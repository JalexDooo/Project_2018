
import warnings

class DefaultConfig(object):
	"""docstring for DefaultConfig"""
	number_of_cpu = -1 # all cpu to use
	

	def _parse(self, kwargs):
		"""
		update config
		"""
		for k, v in kwargs.items():
			if not hasattr(self, k):
				warnings.warn("Warning: opt has not attribute %s" %k)
			setattr(self, k, v)

		print('user config:')

		for k, v in self.__class__.__dict__.items():
			if not k.startswith('_'):
				print(k, getattr(self, k))

opt = DefaultConfig()
