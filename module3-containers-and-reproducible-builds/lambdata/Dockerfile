FROM debian
ENV PYTHONNUNBUFFERED=1
RUN apt-get update && apt-get upgrade -y && \
apt-get install python3-pip curl nano -y && \
pip3 install pandas numpy autopep8 matplotlib && \
pip3 install -i https://test.pypi.org/simple/ lambdata-JoshuaPMallory && \
python3 -c "import lambdata_JoshuaPMallory; print('Its aliiiiive!!!')"