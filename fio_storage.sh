#!/bin/bash
fio 4k_rw.fio > output/fio_4k_rw.txt
fio 32k_rw.fio > output/fio_32k_rw.txt
fio 128k_rw.fio > output/fio_128k_rw.txt