// ***************************************************************
// Copyright (c) 2020 Jittor. Authors: Dun Liang <randonlang@gmail.com>. All Rights Reserved.
// This file is subject to the terms and conditions defined in
// file 'LICENSE.txt', which is part of this source code package.
// ***************************************************************
#pragma once
#include <random>
#include "common.h"

namespace jittor {

typedef void (*set_seed_callback)(int);

void init();
// @pyjt(set_seed, seed)
void set_seed(int seed);

void add_set_seed_callback(set_seed_callback callback);

extern "C"
std::default_random_engine* get_random_engine();

} // jittor
