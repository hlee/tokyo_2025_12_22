# Minimax API Image Generation

This project demonstrates how to use the Minimax API for image generation with proper security practices and error handling.

## Project Structure

```
.
├── .env                    # Contains your API key (excluded from git)
├── .gitignore             # Git ignore file
├── generate_image.py      # Main image generation script
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── *.jpeg               # Generated images (excluded from git)
```

## Setup

### Prerequisites

- Python 3.6 or higher
- pip package manager

### Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Copy your Minimax API key to the `.env` file
   - The file should contain: `MINIMAX_API_KEY=your_api_key_here`

### API Key Setup

The `.env` file should contain your Minimax API key:

```
MINIMAX_API_KEY=your_api_key_here
```

**Important**: The `.env` file is included in `.gitignore` and will not be committed to version control.

## Usage

### Basic Usage

Run the main script to test your API key and generate a sample image:

```bash
python3 generate_image.py
```

### Programmatic Usage

```python
from generate_image import generate_image, save_image

# Generate an image
prompt = "A beautiful sunset over mountains"
images = generate_image(prompt, aspect_ratio="16:9")

# Save the image
if images:
    save_image(images[0], "my_sunset")
```

### Custom Parameters

The `generate_image` function supports the following parameters:

- `prompt` (str): Text description of the image to generate
- `aspect_ratio` (str): Aspect ratio ("16:9", "1:1", "9:16")
- `model` (str): Model to use (default: "image-01")
- `response_format` (str): Response format ("base64" or "url")

## Features

- ✅ Secure API key management using environment variables
- ✅ Comprehensive error handling and logging
- ✅ Multiple test prompts included
- ✅ Automatic image saving with timestamps
- ✅ Proper file organization and git ignore setup
- ✅ Detailed documentation and examples

## API Key Validation

The script includes a test function that validates your API key:

1. Loads the API key from environment variables
2. Makes a test API call with a sample prompt
3. Generates and saves a test image
4. Provides clear success/failure feedback

## Error Handling

The script handles common issues:
- Missing or invalid API keys
- Network connectivity problems
- API service errors
- Invalid response formats

## Generated Images

Images are saved with descriptive filenames including timestamps:
- Format: `{prefix}_{timestamp}.jpeg`
- Example: `minimax_test_1_20251222_161642.jpeg`

## Security Notes

- ✅ API key stored in `.env` (excluded from git)
- ✅ Generated images excluded from version control
- ✅ No sensitive information in code
- ✅ Environment-based configuration

## Dependencies

- `requests>=2.28.0` - HTTP client for API calls
- `python-dotenv>=0.19.0` - Environment variable management

## Testing Status

✅ **API Key Validation**: Successfully tested and working
✅ **Image Generation**: Confirmed functional with test prompt
✅ **File Saving**: Images generated and saved correctly

## Troubleshooting

### Common Issues

1. **"MINIMAX_API_KEY not found"**
   - Ensure the `.env` file exists and contains your API key
   - Check that the API key is correctly formatted

2. **"API request failed"**
   - Verify your API key is valid and not expired
   - Check your internet connection
   - Ensure the Minimax API service is operational

3. **Permission errors**
   - Ensure you have write permissions in the current directory
   - Check that the directory isn't read-only

### Getting Help

If you encounter issues:
1. Check the error message in the console output
2. Verify your API key is correct
3. Ensure all dependencies are installed
4. Test your internet connection

## License

This project is provided as-is for educational and development purposes.
