#!/bin/bash
sudo dpkg --configure -a
sudo apt-get install --yes python3 \
	python3-pip \
	libdpkg-perl \
	cmake \
	python3-dev
	--no-install-recommends

# Make the root lib folders anyone can read
sudo mkdir -p /SEAL
sudo chown ubuntu /SEAL
cp -r ./SEAL /SEAL
cp -r ./SEALExamples /SEALExamples
cp -r ./SEALPython /SEAL
cp -r ./SEALPythonExamples /SEAL

# Build SEAL
cd /SEAL/SEAL
chmod +x configure
sed -i -e 's/\r$//' configure
./configure
make
echo "export LD_LIBRARY_PATH=/SEAL/bin:$LD_LIBRARY_PATH" >> ~/.bashrc

# Build SEAL C++ example
cd /SEAL/SEALExamples
make

# Build SEAL Python wrapper
cd /SEAL/SEALPython
pip3 install setuptools
pip3 install -r requirements.txt
git clone https://github.com/pybind/pybind11.git
cd pybind11
git checkout a303c6fc479662fd53eaa8990dbc65b7de9b7deb
cd ..
python3 setup.py build_ext -i
echo "export PYTHONPATH=$PYTHONPATH:/SEAL/SEALPython:/SEAL/bin" >> ~/.bashrc

# Return to SEAL root directory
cd /SEAL
