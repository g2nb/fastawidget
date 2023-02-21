from nbtools import build_ui
from IPython.display import display


__version__ = '1.0.0'


@build_ui(name='View FASTA File',
          description='Displays a FASTA file using the MSA FASTA viewer.',
          origin='+',
          color='#F37726',
          parameters={
              'fasta_file': {
                  'required': True,
                  'description': 'Select a FASTA file to view',
                  'type': 'file',
                  'kinds': ['fasta']
              }
          })
def view_fasta(fasta_file):
    data = ''
    with open(fasta_file) as f:
        data = f.read()

    display({'application/vnd.fasta.fasta': data}, raw=True)
