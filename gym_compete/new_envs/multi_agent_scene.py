import numpy as np

from gym.envs.mujoco import mujoco_env

class MultiAgentScene(mujoco_env.MujocoEnv):

    def __init__(self, xml_path, n_agents):
        self.n_agents = n_agents
        self._mujoco_init = False
        mujoco_env.MujocoEnv.__init__(self, xml_path, 5)
        self._mujoco_init = True

    def simulate(self, actions):
        a = np.concatenate(actions, axis=0)
        self.do_simulation(a, self.frame_skip)

    def step(self, actions):
        '''
        Just to satisfy mujoco_init, should not be used
        '''
        assert not self._mujoco_init, '_step should not be called on Scene'
        return self._get_obs(), 0, False, None

    def _get_obs(self):
        '''
        Just to satisfy mujoco_init, should not be used
        '''
        assert not self._mujoco_init, '_get_obs should not be called on Scene'
        obs = np.concatenate([
            self.sim.data.qpos.flat,
            self.sim.data.qvel.flat
        ])
        return obs

    def reset_model(self):
        qpos = self.init_qpos + self.np_random.uniform(size=self.model.nq, low=-.1, high=.1)
        qvel = self.init_qvel + self.np_random.randn(self.model.nv) * .1
        self.set_state(qpos, qvel)
        return None

    def viewer_setup(self):
        self.viewer.cam.trackbodyid = 0
        self.viewer.cam.distance = self.model.stat.extent * 0.55
        self.viewer.cam.elevation = -10
        self.viewer.cam.azimuth = 90
        rand = self.np_random.random()
        if rand < 0.33:
            self.viewer.cam.azimuth = 0
        elif 0.33 <= rand < 0.66:
            self.viewer.cam.azimuth = 90
        else:
            self.viewer.cam.azimuth = 180
