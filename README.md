# Slidesgo-scrapper
A small script downloading in full HD every image of a theme (premium or not).

## Installation
`python -m pip install -r requirements.txt`

## Usage
`python scrapper.py <URL theme>` (ex : https://slidesgo.com/theme/acting-agency) 

Externals tags are available : 
``` 
> python scrapper.py --help

NAME
    scrapper.py - This script will scrape the images from the slidesgo theme provided by the url parameter, 
    and save the images with a resolution of min_width x min_height or higher (default is 1600 x 900) 
    in the directory save_dir (default is ./{name_of_the_theme})

SYNOPSIS
    scrapper.py URL <flags>

DESCRIPTION
    This script will scrape the images from the slidesgo theme provided by the url parameter, 
    and save the images with a resolution of min_width x min_height or higher (default is 1600 x 900) 
    in the directory save_dir (default is ./{name_of_the_theme})

POSITIONAL ARGUMENTS
    URL
        Type: str

FLAGS
    --min_width=MIN_WIDTH
        Type: int
        Default: 1600
    --min_height=MIN_HEIGHT
        Type: int
        Default: 900
    -s, --save_dir=SAVE_DIR
        Type: Optional[str]
        Default: None

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS 
``` 
