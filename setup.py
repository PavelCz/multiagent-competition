from os.path import dirname, realpath
from setuptools import find_packages, setup

def read_requirements_file(filename):
    req_file_path = '%s/%s' % (dirname(realpath(__file__)), filename)
    with open(req_file_path) as f:
        return [line.strip() for line in f]

setup(name='gym_compete',
      author='Trapit Bansal et al, with modifications by Adam Gleave, Pavel Czempin',
      version='0.2.1',
      url='https://github.com/PavelCz/multiagent-competition',
      python_requires='>=3.8.0',
      packages=find_packages(exclude=('tests',)),
      package_data={'gym_compete':
        [
          'new_envs/assets/*.xml',
          'agent_zoo/*/*.pkl',
        ],
      },
      install_requires=read_requirements_file('requirements.txt'),
)
