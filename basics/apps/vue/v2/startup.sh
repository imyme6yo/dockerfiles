#!/bin/sh
printf 'y\n' | vue create ${PROJECT} --default
echo ${PROJECT}
cd ${PROJECT}

printf 'y\nn\n' | vue add apollo
printf 'y\n' | vue add router
vue add vuex
