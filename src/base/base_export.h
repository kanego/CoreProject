// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef BASE_BASE_EXPORT_H_
#define BASE_BASE_EXPORT_H_

//#define  _EXPORTING

#ifdef _EXPORTING
#define BASE_EXPORT __declspec(dllexport)
#else
#define BASE_EXPORT __declspec(dllimport)
#endif

#endif
