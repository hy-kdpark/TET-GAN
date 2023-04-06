# Created By  : 박기덕(kdpark@hanyang.co.kr)
# Created Date: 2023/03/09
# Updated Date: 2023/03/10
# version : 1.1
import argparse
import errno
import os
import sys

from PIL import Image, ImageDraw, ImageFont
# pip install pillow

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="TET-GAN용 이미지 제너레이터"
    )
    parser.add_argument(
        "-f",
        "--font",
        type=str,
        nargs="?",
        help="폰트 파일의 경로",
        default="../fonts/NanumMyeongjo.ttf",
    )
    parser.add_argument(
        "-t",
        "--text",
        type=str,
        nargs="?",
        help="생성 글자",
        default="한",
    )
    parser.add_argument(
        "-d",
        "--dir",
        type=str,
        nargs="?",
        help="생성할 결과물의 디렉터리 이름",
        default="../data/content/"
    )
    parser.add_argument(
        "-n",
        "--name",
        type=str,
        nargs="?",
        help="생성할 결과물의 파일 이름",
        default="5.png"
    )
    parser.add_argument(
        "-s",
        "--size",
        type=int,
        nargs="?",
        help="문자의 크기",
        default=160,
    )
    parser.add_argument(
        "-iw",
        "--image_width",
        type=int,
        nargs="?",
        help="결과 이미지의 크기",
        default=256,
    )
    parser.add_argument(
        "-ih",
        "--image_height",
        type=int,
        nargs="?",
        help="결과 이미지의 크기",
        default=256,
    )
    parser.add_argument(
        "-tc",
        "--text_color",
        type=str,
        nargs="?",
        help="글자의 색상 (RGB)",
        default="#ffffff",
    )
    parser.add_argument(
        "-bc",
        "--bg_color",
        type=str,
        nargs="?",
        help="배경 색상 (RGB)",
        default="#000000",
    )
    return parser.parse_args()


def generate(text, typeface, filename, size, width, height, bg_color, text_color):
    try:
        # Create the font
        font = ImageFont.truetype(typeface, size)
        # New image based on the settings defined above
        img = Image.new("RGB", (width, height), color=bg_color)
        # Interface to draw on the image
        draw_interface = ImageDraw.Draw(img)

        if font.getmask(text).getbbox() != None:
            # Calculate x, y
            w, h = font.getsize(text)
            x = (width - w) / 2
            y = (height - h) / 2
            # print(x, y)
            # Draw text
            draw_interface.text((x, y), text, font=font, fill=text_color)
            # Save the result image
            if os.path.exists(filename):
                os.remove(filename)
            img.save("{0}".format(filename))
    except OSError:
        return


def main():
    # Argument parsing
    args = parse_arguments()

    # Creating char list
    text = []
    if args.text:
        text = args.text
    else:
        sys.exit("Cannot find text!")

    # Check font
    if args.font and os.path.exists(args.font):
        font = args.font
    else:
        sys.exit("Cannot find font!")

    # Check image size
    if args.size > args.image_width:
        width = args.size
    else:
        width = args.image_width
    if args.size > args.image_height:
        height = args.image_width
    else:
        height = args.image_height

    filename = os.path.join(args.dir, args.name)

    # Generate char list
    generate(text, font, filename, args.size, width, height, 
             args.bg_color, args.text_color)


if __name__ == "__main__":
    main()
