# cflags and cflags_cc will not work on MacOS. See
# https://github.com/nodejs/node/blob/main/common.gypi
# for how to set compiler flags on different platforms.

# pylint: disable-next=pointless-statement
{
  'targets': [{
    'target_name': 'hello_world_binding',
    'sources': ['binding/hello_world_binding.cc'],
    'include_dirs': ["<!(node -p \"require('node-addon-api').include_dir\")"],
    'defines': [
      'NAPI_DISABLE_CPP_EXCEPTIONS',
      'NAPI_VERSION=<(napi_build_version)',
      'NODE_ADDON_API_ENABLE_MAYBE',
    ],
    'conditions': [[
      'OS=="mac"',
      {
        'cflags+': ['-fvisibility=hidden'],
        'xcode_settings': {
          'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES',  # -fvisibility=hidden
        }
      }
    ]]
  }],
}
