docker run --rm --gpus '"device=1"' --name TET-GAN \
	-w /workspace -v $PWD:/workspace --shm-size=32G --network=host \
	-it pytorch/pytorch:1.8.0-cuda11.1-cudnn8-devel \
	/bin/bash -c "source /workspace/preprocess.sh && bash"
