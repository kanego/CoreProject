# Copyright (c) 2014 The CoreProject Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets':
  [
    {
      'target_name'     : 'base',
      'type'            : 'static_library',
      'msvs_guid'       : '6013D884-A9D6-451F-9A99-BC2F3C0EADED',
      'dependencies'    : '',
      'include_dirs'    :
      [
        '',
      ],
      'sources'         :
      [
        'src/base/memory/shared_memory.h',
        'src/base/memory/shared_memory.cc',
        'src/base/memory/linked_ptr.h',
        'src/base/memory/raw_scoped_refptr_mismatch_checker.h',
        'src/base/memory/ref_counted.h',
        'src/base/memory/ref_counted.cpp',
        'src/base/memory/ref_counted_memory.h',
        'src/base/memory/ref_counted_memory.cpp',
        'src/base/memory/scoped_handle.h',
        'src/base/memory/scoped_open_process.h',
        'src/base/memory/scoped_ptr.h',
        'src/base/memory/scoped_vector.h',
        'src/base/memory/singleton.h',
        'src/base/memory/weak_ptr.h',
        'src/base/memory/weak_ptr.cpp',

        'src/base/debug/debugger.h',
        'src/base/debug/debugger.cpp',
        'src/base/debug/stack_trace.h',
        'src/base/debug/stack_trace.cpp',

        'src/base/process/process.h',
        'src/base/process/process.cc',
        'src/base/process/process_util.h',
        'src/base/process/process_util.cc',

        'src/base/win/windows_version.h',
        'src/base/win/windows_version.cpp',
        'src/base/win/object_watcher.h',
        'src/base/win/object_watcher.cpp',
        'src/base/win/registry.h',
        'src/base/win/registry.cpp',
        'src/base/win/resource_util.h',
        'src/base/win/resource_util.cpp',
        'src/base/win/scoped_bstr.h',
        'src/base/win/scoped_bstr.cpp',
        'src/base/win/scoped_comptr.h',
        'src/base/win/scoped_gdi_object.h',
        'src/base/win/scoped_co_mem.h',
        'src/base/win/scoped_handle.h',
        'src/base/win/scoped_hdc.h',
        'src/base/win/scoped_hglobal.h',
        'src/base/win/scoped_variant.h',
        'src/base/win/scoped_variant.cpp',
        'src/base/win/win_util.h',
        'src/base/win/win_util.cpp',
        'src/base/win/wrapped_window_proc.h',
        'src/base/win/wrapped_window_proc.cpp',

        'src/base/log/logging.h',
        'src/base/log/logging.cpp',
        'src/base/log/vlog.h',
        'src/base/log/vlog.cpp',


        'src/base/time/time.h',
        'src/base/time/time.cpp',
        'src/base/time/timer.h',
        'src/base/time/timer.cpp',

        'src/base/task/task.h',
        'src/base/task/task.cpp',
        'src/base/task/task_queue.h',
        'src/base/task/task_queue.cpp',

        'src/base/string/utf_string_conversions.h',
        'src/base/string/utf_string_conversions.cpp',
        'src/base/string/string_piece.h',
        'src/base/string/string_piece.cpp',
        'src/base/string/string16.h',

        'src/base/files/file_path.h',
        'src/base/files/file_path.cpp',
        'src/base/files/file_util.h',
        'src/base/files/file_util.cpp',
        'src/base/files/file_version_info.h',
        'src/base/files/file_version_info.cpp',
        'src/base/files/platform_file.h',
        'src/base/files/platform_file.cpp',
        'src/base/files/scoped_temp_dir.h',
        'src/base/files/scoped_temp_dir.cpp',

        'src/base/metric/histogram.h',
        'src/base/metric/histogram.cpp',
        'src/base/metric/stats_counters.h',
        'src/base/metric/stats_counters.cpp',
        'src/base/metric/stats_table.h',
        'src/base/metric/stats_table.cpp',
        'src/base/metric/field_trial.h',
        'src/base/metric/field_trial.cpp',

        'src/base/threading/non_thread_safe.h',
        'src/base/threading/non_thread_safe_impl.h',
        'src/base/threading/non_thread_safe_impl.cpp',
        'src/base/threading/platform_thread.h',
        'src/base/threading/platform_thread.cpp',
        'src/base/threading/thread.h',
        'src/base/threading/thread.cpp',
        'src/base/threading/thread_checker.h',
        'src/base/threading/thread_checker_impl.h',
        'src/base/threading/thread_checker_impl.cpp',
        'src/base/threading/thread_local.h',
        'src/base/threading/thread_local.cpp',
        'src/base/threading/thread_local_storage.h',
        'src/base/threading/thread_local_storage.cpp',
        'src/base/threading/thread_restrictions.h',
        'src/base/threading/thread_restrictions.cpp',

        'src/base/synchronization/condition_variable.h',
        'src/base/synchronization/condition_variable.cpp',
        'src/base/synchronization/lock.h',
        'src/base/synchronization/lock.cpp',
        'src/base/synchronization/lock_impl.h',
        'src/base/synchronization/lock_impl.h',
        'src/base/synchronization/waitable_event.h',
        'src/base/synchronization/waitable_event.cpp',
        'src/base/synchronization/waitable_event_watcher.h',
        'src/base/synchronization/waitable_event_watcher.cpp',

        'src/base/sql/',
        'src/base/base_export.h',
        'src/base/basic_types.h',
        'src/base/port.h',
        'src/base/pickle.h',
        'src/base/pickle.cpp',
        'src/base/atomicops.h',
        'src/base/path_service.h',
        'src/base/path_service.cpp',
        'src/base/base_path.h',
        'src/base/base_path.cpp',
        'src/base/base_switches.h',
        'src/base/base_switches.cpp',




        'publicdef/config_define.h',
      ],
      'include_dirs'   : 
      [
        'publicdef/',
        '../',
        '../../',
        'src/',
        'src/base/',
      ],

      'defines'        :
      [
        'OS_WIN=1',
      ],
      'msvs_disabled_warnings'       : [4018, 4005, 4482, 4190, 4067],
      'msvs_configuration_attributes': 
	  {
        'UseOfATL': '2',
      },
      'configurations'               : 
      {
        'Common_Base': 
        {
          'msvs_configuration_attributes': 
          {
          },
        },
       'Debug': 
        {
          'msvs_settings': 
          {
              'VCCLCompilerTool': 
              {
                'DebugInformationFormat': '3',
                'ProgramDataBaseFileName': '',
              },
          },
        },
        'Release': 
        {
          'msvs_settings': 
          {
              'VCCLCompilerTool': 
              {
                'DebugInformationFormat': '3',
                'ProgramDataBaseFileName': '',
              },
          },
        },
      },     
    },
  ],
}
