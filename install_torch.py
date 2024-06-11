import subprocess
import sys


def check_nvidia_gpu():
    try:
        output = subprocess.check_output(["nvidia-smi"], stderr=subprocess.STDOUT)
        return "NVIDIA" in output.decode("utf-8")
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError:
        return False


def install_packages():
    # Install common dependencies
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
    )

    gpu_available = check_nvidia_gpu()
    if gpu_available:
        # Install the GPU version of PyTorch
        subprocess.check_call(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "torch==2.0.1+cu118",
                "-f",
                "https://download.pytorch.org/whl/torch_stable.html",
            ]
        )
    else:
        # Install the CPU version of PyTorch
        subprocess.check_call([sys.executable, "-m", "pip", "install", "torch"])


if __name__ == "__main__":
    install_packages()
