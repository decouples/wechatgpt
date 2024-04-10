#!/bin/bash

unset KUBECONFIG

cd .. && docker build -f docker/Dockerfile -t wechatgpt:$(date +%y%m%d) .
