class Path(object):
    @staticmethod
    def db_root_dir(dataset):
        if dataset == 'TunnelCrack':
            return '/home/models/LinkCrack/data/TunnelCrack/'
        else:
            print('Dataset {} not available.'.format(dataset))
            raise NotImplementedError