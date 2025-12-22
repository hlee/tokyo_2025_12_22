import base64
import requests
import os
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def generate_image(prompt, aspect_ratio="16:9", model="image-01", response_format="base64"):
    """
    Generate an image using Minimax API
    
    Args:
        prompt (str): Text description of the image to generate
        aspect_ratio (str): Aspect ratio of the image (e.g., "16:9", "1:1", "9:16")
        model (str): Model to use for generation
        response_format (str): Format of the response ("base64" or "url")
    
    Returns:
        list: List of base64 encoded images
    """
    url = "https://api.minimax.io/v1/image_generation"
    api_key = os.environ.get("MINIMAX_API_KEY")
    
    if not api_key:
        raise ValueError("MINIMAX_API_KEY not found in environment variables")
    
    headers = {"Authorization": f"Bearer {api_key}"}
    
    payload = {
        "model": model,
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "response_format": response_format,
    }
    
    try:
        print(f"Generating image with prompt: {prompt[:50]}...")
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        
        result = response.json()
        
        if response_format == "base64":
            images = result["data"]["image_base64"]
            return images
        else:
            images = result["data"]["image_url"]
            return images
            
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        if hasattr(e.response, 'text'):
            print(f"Response: {e.response.text}")
        raise
    except KeyError as e:
        print(f"Unexpected response format: {e}")
        print(f"Response: {result}")
        raise

def save_image(image_data, filename_prefix="generated_image"):
    """
    Save base64 encoded image to file
    
    Args:
        image_data (str): Base64 encoded image data
        filename_prefix (str): Prefix for the output filename
    
    Returns:
        str: Filename of the saved image
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.jpeg"
    
    try:
        with open(filename, "wb") as f:
            f.write(base64.b64decode(image_data))
        print(f"Image saved as: {filename}")
        return filename
    except Exception as e:
        print(f"Failed to save image: {e}")
        raise

def main():
    """Main function to test the Minimax API"""
    
    # Test prompts
    test_prompts = [
        "men Dressing in white t shirt, full-body stand front view image :25, outdoor, Venice beach sign, full-body image, Los Angeles, Fashion photography of 90s, documentary, Film grain, photorealistic",
        "A serene mountain landscape at sunrise, golden light, misty valleys, professional photography",
        "A futuristic city with flying cars, neon lights, cyberpunk style, detailed architecture"
    ]
    
    print("Testing Minimax API Key...")
    print("=" * 50)
    
    try:
        # Test with the first prompt
        prompt = test_prompts[0]
        images = generate_image(prompt)
        
        if images:
            print(f"✅ API key is working! Generated {len(images)} image(s)")
            
            # Save all generated images
            for i, image_data in enumerate(images):
                filename_prefix = f"minimax_test_{i+1}"
                save_image(image_data, filename_prefix)
            
            print("\n" + "=" * 50)
            print("🎉 Test completed successfully!")
            print(f"Generated {len(images)} image(s) using the provided API key")
            
        else:
            print("❌ No images were generated")
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        print("\nPossible issues:")
        print("- API key is invalid or expired")
        print("- Network connectivity issues")
        print("- API service is down")
        print("- Request parameters are incorrect")

if __name__ == "__main__":
    main()
