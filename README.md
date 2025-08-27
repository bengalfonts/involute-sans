# Involute Sans

A contemporary Bangla & English geometric sans-serif typeface, crafted with precision and mathematical harmony for today’s digital and print world.

## Overview

Involute Sans is the result of a unique collaboration between Involute Tech, founded by Nowab Md. Aminul Haq, and Bengal Fonts, led by Thouhedul Islam Himel. Rooted in the harmony of the Fibonacci sequence and the Golden Ratio, each character, Bangla and Latin alike has been meticulously shaped to achieve balance, rhythm, and timeless elegance.

Designed to perform seamlessly in both digital and print applications, Involute Sans offers clarity, efficiency, and versatility making it ideal for corporate branding, web design, software UI, editorial content, and presentations. Its geometry conserves space while maintaining readability and visual refinement.

More than just a typeface, Involute Sans reflects the shared vision of Involute Tech and Bengal Fonts: to merge innovation, mathematics, and Bengali cultural identity into a design system that speaks with professionalism and artistry.

## Font Files

This project contains the following font formats:
- **InvoluteSans-Regular.otf** - OpenType font (source)
- **InvoluteSans-Regular.ttf** - TrueType font
- **InvoluteSans-Regular.woff** - Web Open Font Format
- **InvoluteSans-Regular.woff2** - Web Open Font Format 2.0

## Project Structure

```
involute-sans/
├── fonts/                    # Compiled font files
│   ├── ttf/                 # TrueType fonts
│   ├── woff/                # WOFF fonts
│   └── woff2/               # WOFF2 fonts
├── sources/                  # Source font files
│   └── InvoluteSans-Regular.otf
├── METADATA.pb              # Google Fonts metadata
├── DESCRIPTION               # Font description
├── OFL.txt                  # Open Font License
├── README.md                # This file
└── build.py                 # Build script
```

## Setup

### Prerequisites

1. Python 3.7+
2. Google Fonts tools
3. FontTools

### Installation

```bash
# Clone the repository
git clone https://github.com/googlefonts/involute-sans.git
cd involute-sans

# Install dependencies
pip install fonttools
pip install gftools

# Install Google Fonts tools
pip install gftools
```

## Building Fonts

### Using the Build Script

```bash
python build.py
```

This will:
- Generate TTF files from source OTF files
- Create WOFF and WOFF2 web fonts
- Organize files into the proper directory structure
- Validate font files

### Manual Build

```bash
# Generate TTF from OTF
fonttools ttLib.otf2ttf sources/InvoluteSans-Regular.otf fonts/ttf/InvoluteSans-Regular.ttf

# Generate WOFF
fonttools ttLib.woff2compress fonts/ttf/InvoluteSans-Regular.ttf fonts/woff/InvoluteSans-Regular.woff

# Generate WOFF2
fonttools ttLib.woff2compress fonts/ttf/InvoluteSans-Regular.ttf fonts/woff2/InvoluteSans-Regular.woff2
```

## Usage

### Web Fonts

```css
@font-face {
  font-family: 'Involute Sans';
  src: url('fonts/woff2/InvoluteSans-Regular.woff2') format('woff2'),
       url('fonts/woff/InvoluteSans-Regular.woff') format('woff'),
       url('fonts/ttf/InvoluteSans-Regular.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

body {
  font-family: 'Involute Sans', sans-serif;
}
```

### Desktop Applications

Install the TTF or OTF files in your system's font directory:

- **macOS**: `/Library/Fonts/` or `~/Library/Fonts/`
- **Windows**: `C:\Windows\Fonts\`
- **Linux**: `~/.local/share/fonts/` or `/usr/share/fonts/`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the fonts
5. Submit a pull request

## License

This project is licensed under the SIL Open Font License, Version 1.1. See [OFL.txt](OFL.txt) for details.

## Support

For questions and support, please open an issue on GitHub or contact the project maintainers.

## Designers & Contributors

### Bengal Fonts Team
- **Thouhedul Islam Himel**
  - Lead Type Designer & Founder of Bengal Fonts
  - Email: himel.bengalfonts@gmail.com
  - Thouhedul Islam Himel is a visionary Bangladeshi type designer and the Founder of Bengal Fonts. With a deep understanding of Bangla typography and cultural aesthetics, he blends tradition with modern innovation to create typefaces that are functional, artistic, and timeless. His dedication to advancing Bangla type design continues to shape the future of typography in Bangladesh. 
  - More of his works are available at bengalfonts.com

- **Kazi Nasirul Islam**
  - Associate Type Developer, Bengal Fonts
  - Email: bengalfonts@gmail.com

### Involute Team
- **Nowab Md. Aminul Haq**
  - Founder, Involute Tech
  - Email: business@involutebd.com

  - **Safa Tus Selahin Raj**
  - Designer, Involute Tech
  - Email: business@involutebd.com

  - **Studio Shwo**
  - Uppercase Character Set Design
  - Email: studioshwo@gmail.com


### Organizations
- **Bengal Fonts** - Bengal Fonts is the first type foundry from Bangladesh, dedicated to developing high-quality Bangla and multilingual typefaces. With a mission to preserve cultural heritage while embracing modern design, it delivers reliable, professional, and visually harmonious fonts for both digital and print media.

- **Involute Tech** - Involute Tech is a Bangladesh-based technology company focused on innovation, digital solutions, and future-driven design. With a vision to merge technology and creativity, Involute Tech delivers reliable services and forward-looking products that empower businesses and enhance user experiences.


## Acknowledgments

- Font Designer: [Thouhedul Islam Himel]
- Contributors: [Nowab Md. Aminul Haq, Kazi Nasirul Islam, Studio Shwo]
- Special thanks to the Google Fonts team for their tools and support
   