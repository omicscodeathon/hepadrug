from modeller import *
from modeller.automodel import *    # Load the AutoModel class

log.verbose()
env = Environ()

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

class MyModel(AutoModel):
    def select_atoms(self):
        return Selection(self.residue_range('27:A', '41:A'),
                         self.residue_range('232:A', '232:A'))

a = MyModel(env, alnfile = 'alignment.ali',
            knowns = '1qg8', sequence = '1qg8_fill')
a.starting_model= 1
a.ending_model  = 1

a.make()