#!/bin/bash
apt update
apt install -y libgl1-mesa-glx libglib2.0-0
pip install matplotlib scipy opencv-python Pillow
pip install gradio --use-feature=2020-resolver
