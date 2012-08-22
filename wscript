import os

srcdir = '.'
blddir = 'build'
VERSION = '0.0.1'

def set_options(opt):
  opt.tool_options('compiler_cxx')

def configure(conf):
  conf.check_tool('compiler_cxx')
  conf.check_tool('node_addon')
  conf.env.append_unique('CXXFLAGS', ['-Wall', '-O3'])
  conf.env['ERIZO_HOME'] = os.environ['ERIZO_HOME']

def build(bld):
  obj = bld.new_task_gen('cxx', 'shlib', 'node_addon')
  obj.cxxflags = ["-I"+bld.env['ERIZO_HOME']+"/src/erizo", "-g", "-Wall"]
  obj.target = 'addon'
  obj.source = ['addon.cc', 'WebRtcConnection.cc', 'OneToManyProcessor.cc']
  bld.env.append_value('LINKFLAGS',('-L'+bld.env['ERIZO_HOME'] + "/build/erizo/ -lerizo").split())
