# AI-Automated Ad Copy Generator

This project implements an automated ad copy generator using the Hugging Face API and the GPT-2 XL model. It's designed to create targeted advertising copy, with a particular focus on eco-friendly products.

## Features

- Generation of ad copy based on specific inputs (product, target audience, tone)
- Performance analysis of the generated copy based on provided metrics
- Utilization of the Hugging Face API for natural language processing

## Requirements

- Python 3.7+
- A Hugging Face API key (free, but with usage limits)

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/simonedimeglio/ai-automated-ad-copy-generator.git
   cd ai-automated-ad-copy-generator
   ```

2. Create a virtual environment and activate it:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Create a `config.py` file in the root directory and add your Hugging Face API key:
   ```python
   HUGGINGFACE_API_KEY = "your_api_key_here"
   ```

## Usage

Run the example script to generate an ad copy and analyze its performance:

```
python examples/generate_ad_copy.py
```

You can modify the input parameters in the script to generate different types of ad copy.

## Project Structure

```
ai-automated-ad-copy-generator/
│
├── src/
│   ├── __init__.py
│   ├── ad_copy_generator.py
│   ├── huggingface_interface.py
│   └── utils.py
├── examples/
│   └── generate_ad_copy.py
├── tests/
│   └── test_ad_copy_generator.py
├── .gitignore
├── README.md
├── requirements.txt
└── config.py
```

## Known Limitations

- The free tier of the Hugging Face API has usage limits, which may restrict the number of requests you can make per hour.
- The quality of the generated ad copy may vary and might require human review and editing.
- The performance analysis is based on a simple prompt and may not provide in-depth insights.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Disclaimer

This project is for educational purposes only. The generated ad copy should be reviewed and edited by a human before use in any real-world applications.
