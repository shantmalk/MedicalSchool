""" 
MEDICAL SCHOOL

DATE CREATED:  2018-07-29

LECTURES COVERED:

LECTURE ID        |                    FILE NAME              |    PROFESSOR
    A             |07302018_AminoAcidsProteinStructure_notes_2|    Ackerman

[ADD]

LEARNING OBJECTIVES:

A1.  State the names, 1-letter code, and 3-letter code of the 20 common amino acids.
A2.  Classify the amino acids based on their chemical structure and charge at neutral pH
and predict their behavior in an electrical field.
A3.  Calculate the isoelectric point (pI) of a molecule with ionizable groups.
A4.  Describe the features of the peptide bond and its impact on protein structures.

[ADD]
"""
import os




class AminoAcid:
    def __init__(self, aa_fp, pH=7.0 ):
        self._import_amino_acid(aa_fp)
        self.cur_pH = pH
    
    def _import_amino_acid(self, fp):
        with open(fp, 'r') as curfile:
            aa_data = curfile.readlines()
        self.chem_struct_str = self._load_info(aa_data, ['STRUCTURE:','NAME:'], False)
        self.name_str = self._load_info(aa_data, ['NAME:','ABBREVIATION:'])
        self.abbrev_str = self._load_info(aa_data, ['ABBREVIATION:','LETTER:'])
        self.letter_str = self._load_info(aa_data, ['LETTER:','pK:'])
        self.pK_str = self._load_info(aa_data, ['pK:','pI:'], False)
        self.pK_NH3 = float(self.pK_str.split(sep='\n')[0].strip())
        self.pK_COOH = float(self.pK_str.split(sep='\n')[1].strip())
        self.pK_R = float(self.pK_str.split(sep='\n')[2].strip())
        self.pI = float(self._load_info(aa_data, ['pI:','\n']))
        self._parse_charge()
        
    def _load_info(self, cur_data, str_keys, clean=True):
        label_start = str_keys[0]
        label_end = str_keys[1]
        info_str = ''
        str_add = False
        for ln_num in range(len(cur_data)):
            if cur_data[ln_num] == '\n':
                continue
            clean_ln = cur_data[ln_num].replace('\n', '').strip()
            if clean_ln == label_end:
                break
            if str_add:
                if clean:
                    info_str += cur_data[ln_num].replace('\n', '').strip()
                else:
                    info_str += cur_data[ln_num]
            if clean_ln == label_start:
                str_add = True
        return info_str.rstrip('\n')
    
    
    def _update_chem_struct_str(self, chem_struct_str):
        #NH3 GROUP
        pass
              
            
    def _parse_charge(self):
        conv_sign = {'+' : 1 , '-' : -1, ' ' : ' '}
        chem_struct_ls = self.chem_struct_str.split('\n')
        charge_NH2_idx = [1, chem_struct_ls[1].find('+')]
        charge_COOH_idx = [1, charge_NH2_idx[1] + 9]
        
        self.cur_N_charge = conv_sign[chem_struct_ls[charge_NH2_idx[0]][charge_NH2_idx[1]]]
        cur_len = len(chem_struct_ls[1])
        if cur_len < charge_COOH_idx[1]:
            self.cur_COOH_charge = 0
            chem_struct_ls[1] = chem_struct_ls[1][cur_len: ] + ' '*(charge_COOH_idx[1]-cur_len)
            self.chem_struct_str = ''.join(chem_struct_ls)
        else:
            self.cur_COOH_charge = conv_sign[chem_struct_ls[charge_COOH_idx[0]][charge_COOH_idx[1]]]
    
    
    def _update_charge(self, group, charge ):
        chem_struct_ls = self.chem_struct_str.split('\n')
        if group == 'AMINE':
            charge_amine_idx = [1, chem_struct_ls[2].find('N')]
            if charge == 0:
                chem_struct_ls[charge_amine_idx[0]][charge_amine_idx[1]] = ' '
                chem_struct_ls[charge_amine_idx[0]+1][charge_amine_idx[1]-1] = '2'
            elif charge == 1:
                chem_struct_ls[charge_amine_idx[0]][charge_amine_idx[1]] = '+'
                chem_struct_ls[charge_amine_idx[0]+1][charge_amine_idx[1]-1] = '3'
        elif group == 'CARBOXYLIC':
            charge_carboxyl_idx = [1, chem_struct_ls[2].find('OH')]
            if charge == 0:
                chem_struct_ls[charge_carboxyl_idx[0]][charge_carboxyl_idx[1]] = ' '
            elif charge == 
        elif group == 'R':
            pass
        
    def __repr__(self):
        return self.letter_str
    
    def __str__(self):
        return '''
{NAME} ({ABBREV}, {LETTER})
{CHEM_STRUCT}

pK NH3: {pK_NH}
pK COOH: {pK_COOH}
pK R: {pK_R}

pI: {pI}
        '''.format(NAME=self.name_str, ABBREV=self.abbrev_str, LETTER=self.letter_str,
                   CHEM_STRUCT=self.chem_struct_str, pK_NH=self.pK_NH3, pK_COOH=self.pK_COOH,
                   pK_R=self.pK_R, pI=self.pI)


def init_amino_acids():
    cwd = os.getcwd() + '\\..\\..\\amino_acids'
    aa_fnames = ['alanine',
                 'asparagine',
                 'aspartic_acid',
                 'glutamic_acid',
                 'glutamine',
                 'glycine',
                 'isoleucine',
                 'methionine',
                 'phenylalanine',
                 'proline',
                 'serine',
                 'threonine',
                 'tryptophan',
                 'tyrosine',
                 'valine',
                 'cysteine',
                 'lysine',
                 'histidine'
                 ]
    aa_fnames.sort()
    amino_acids = []
    for aa in aa_fnames:
        amino_acids.append(AminoAcid(os.path.join(cwd, aa)))
    return amino_acids


def run_lectureA():
    """
    Simple function that will display amino acid structure (A1) at varying pHs
    (pH 3, 7, and 11) (A2-A4)
    """
    amino_acids = init_amino_acids()
    amino_acids.sort(key=lambda x : x.pI)
#     [print(x) for x in amino_acids]
    
if __name__ == '__main__':
    run_lectureA()

    
    