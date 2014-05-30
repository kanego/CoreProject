// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef   CONFIG_DEFINE_H_
#define   CONFIG_DEFINE_H_

#define OS_WIN 1
#define UNICODE

#define COMPILER_MSVC       1

#if defined(_M_X64) || defined(__x86_64__)
#define ARCH_CPU_X86_FAMILY 1
#define ARCH_CPU_X86_64     1
#define ARCH_CPU_64_BITS    1
#elif defined(_M_IX86) || defined(__i386__)
#define ARCH_CPU_X86_FAMILY 1
#define ARCH_CPU_X86        1
#define ARCH_CPU_32_BITS    1
#endif

#define OVERRIDE override

#endif