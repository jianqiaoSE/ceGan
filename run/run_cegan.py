
# Copyright (C), 2018-下午2:52
# FileName: run_cegan.py
# Author:   b8313
# Date:     下午2:52 下午2:52
# Description:
#

import sys
from subprocess import call
import argparse

import os

"""
this part of code was copied from rel-gan

"""

# Job id and gpu_id
# if len(sys.argv) > 2:
#     job_id = int(sys.argv[1])
#     gpu_id = str(sys.argv[2])
#     print('job_id: {}, gpu_id: {}'.format(job_id, gpu_id))
# elif len(sys.argv) > 1:
#     job_id = int(sys.argv[1])
#     gpu_id = 0
#     print('job_id: {}, missing gpu_id (use default {})'.format(job_id, gpu_id))
# else:
#     job_id = 1
#     gpu_id = 0
#     print('Missing argument: job_id and gpu_id. Use default job_id: {}, gpu_id: {}'.format(job_id, gpu_id))


job_id = 1
gpu_id = 0
print('Missing argument: job_id and gpu_id. Use default job_id: {}, gpu_id: {}'.format(job_id, gpu_id))

# Executables
executable = 'python'  # specify your own python interpreter path here
rootdir = '../'
scriptname = 'main.py'

# ===Program===
if_test = int(False)
run_model = 'cegan'
CUDA = int(True)
oracle_pretrain = int(True)
gen_pretrain = int(False)
dis_pretrain = int(False)
MLE_train_epoch = 30
ADV_train_epoch = 3000
tips = 'CeGAN experiments'

# ===Oracle or Real===
if_real_data = [int(False), int(True), int(True)]
dataset = ['oracle', 'image_coco', 'emnlp_news']
loss_type = 'ragan'
vocab_size = [5000, 0, 0]
temp_adpt = 'sqrt'
temperature = [1, 100, 100]

# ===Basic Param===
data_shuffle = int(False)
model_type = 'RMC'
gen_init = 'truncated_normal'
dis_init = 'uniform'
samples_num = 10000
# batch_size = 32
batch_size = 32
max_seq_len = 20
gen_lr = 0.01
gen_adv_lr = 1e-4
dis_lr = 1e-4
pre_log_step = 10
adv_log_step = 50
mu_temp = 'exp'

# ===Generator===
ADV_g_step = 1
gen_embed_dim = 32
gen_hidden_dim = 32
mem_slots = 1
num_heads = 2
head_size = 256

# ===Discriminator===
ADV_d_step = 5
dis_embed_dim = 64
dis_hidden_dim = 64
num_rep = 64

# ===Metrics===
use_nll_oracle = int(True)
use_nll_gen = int(True)
use_nll_div = int(True)
use_bleu = int(True)
use_self_bleu = int(True)
use_ppl = int(False)


def program_config(parser):
    parser.add_argument('--mu_temp', default=mu_temp, type=str)
    parser.add_argument('--temp', default=temperature[job_id], type=int)
    parser.add_argument('--fn_mu_temp', default=mu_temp, type=str)
    return parser


parser = argparse.ArgumentParser()
parser = program_config(parser)
opt = parser.parse_args()


args = [
    # Program
    '--if_test', if_test,
    '--run_model', run_model,
    '--cuda', CUDA,
    # '--device', gpu_id,   # comment for auto GPU
    '--ora_pretrain', oracle_pretrain,
    '--gen_pretrain', gen_pretrain,
    '--dis_pretrain', dis_pretrain,
    '--mle_epoch', MLE_train_epoch,
    '--adv_epoch', ADV_train_epoch,
    '--tips', tips,

    # Oracle or Real
    '--if_real_data', if_real_data[job_id],
    '--dataset', dataset[job_id],
    '--loss_type', loss_type,
    '--vocab_size', vocab_size[job_id],
    '--temp_adpt', temp_adpt,
    # '--temperature', temperature[job_id],
    '--temperature', opt.temp,
    '--mu_temp', opt.mu_temp,
    '--fn_mu_temp',opt.fn_mu_temp,

    # Basic Param
    '--shuffle', data_shuffle,
    '--model_type', model_type,
    '--gen_init', gen_init,
    '--dis_init', dis_init,
    '--samples_num', samples_num,
    '--batch_size', batch_size,
    '--max_seq_len', max_seq_len,
    '--gen_lr', gen_lr,
    '--gen_adv_lr', gen_adv_lr,
    '--dis_lr', dis_lr,
    '--pre_log_step', pre_log_step,
    '--adv_log_step', adv_log_step,

    # Generator
    '--adv_g_step', ADV_g_step,
    '--gen_embed_dim', gen_embed_dim,
    '--gen_hidden_dim', gen_hidden_dim,
    '--mem_slots', mem_slots,
    '--num_heads', num_heads,
    '--head_size', head_size,

    # Discriminator
    '--adv_d_step', ADV_d_step,
    '--dis_embed_dim', dis_embed_dim,
    '--dis_hidden_dim', dis_hidden_dim,
    '--num_rep', num_rep,

    # Metrics
    '--use_nll_oracle', use_nll_oracle,
    '--use_nll_gen', use_nll_gen,
    '--use_nll_div', use_nll_div,
    '--use_bleu', use_bleu,
    '--use_self_bleu', use_self_bleu,
    '--use_ppl', use_ppl,

]

args = list(map(str, args))
my_env = os.environ.copy()
call([executable, scriptname] + args, env=my_env, cwd=rootdir)
