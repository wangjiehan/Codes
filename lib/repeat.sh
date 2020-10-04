#!/bin/bash

# 定义repeat函数,执行命令,直到成功 
function repeat()
{
    while true
    do
        $@ && return
    done
}

# 调用repeat函数执行命令
repeat git pull