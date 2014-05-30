@echo off

pushd %~dp0

if exist build rmdir /s/q build

mkdir build

python msvs_gyp_wrapper.py --depth=build -f msvs -I common.gypi --generator-output=build -G msvs_version=2010 -D msvs_gyp_wrapper.gyp

call build\coreProject.sln  startenv debug

popd
