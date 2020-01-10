f=open('test.pdb', 'r')
for line in f:
    aminoacid_name=line[17:20]
    atom_name=line[13:16]
    '''X=line[31:39]
    Y=line[40:47]
    Z=line[47:55]'''

    if aminoacid_name=='LEU':
        if atom_name=='N  ':
            xN=float(line[31:38])
            yN=float(line[39:46])
            zN=float(line[47:54])
            N_koordinates=[xN, yN, zN]
            print(N_koordinates)
        if atom_name=='CA ':
            xCA=float(line[31:38])
            yCA=float(line[39:46])
            zCA=float(line[47:54])
            CA_koordinates=[xCA, yCA, zCA]
            print(CA_koordinates)
        if atom_name=='C  ':
            xC=float(line[31:38])
            yC=float(line[39:46])
            zC=float(line[47:54])
            C_koordinates=[xC, yC, zC]
            print(C_koordinates)
        if atom_name=='O  ':
            xO=float(line[31:38])
            yO=float(line[39:46])
            zO=float(line[47:54])
            O_koordinates=[xO, yO, zO]
            print(O_koordinates)
        if atom_name=='CB ':
            xCB=float(line[31:38])
            yCB=float(line[39:46])
            zCB=float(line[47:54])
            CB_koordinates=[xCB, yCB, zCB]
            print(CB_koordinates)
        if atom_name=='CG ':
            xCG=float(line[31:38])
            yCG=float(line[39:46])
            zCG=float(line[47:54])
            CG_koordinates=[xCG, yCG, zCG]
            print(CG_koordinates)
        if atom_name=='CD1':
            xCD1=float(line[31:38])
            yCD1=float(line[39:46])
            zCD1=float(line[47:54])
            CD1_koordinates=[xCD1, yCD1, zCD1]
            print(CD1_koordinates)
        if atom_name=='CD2':
            xCD2=float(line[31:38])
            yCD2=float(line[39:46])
            zCD2=float(line[47:54])
            CD2_koordinates=[xCD2, yCD2, zCD2]
            print(CD2_koordinates)
            x_sum=xN+xCA+xC+xO+xCB+xCG+xCD1+xCD2
            x_numerator=(xCA+xCB+xCG+xCD1+xCD2+xC)*12+xN*14+xO*16
            x_center=float(x_numerator/x_sum)
            y_sum=yN+yCA+yO+yCB+yCG+yCD1+yCD2+yC
            y_numerator=(yCA+yCB+yCG+yCD1+yCD2+yC)*12+yN*14+yO*16
            y_center=float(y_numerator/y_sum)
            z_sum=zN+zCA+zO+zCB+zCG+zCD1+zCD2+zC
            z_numerator=(zCA+zCB+zCG+zCD1+zCD2+zC)*12+zN*14+zO*16
            z_center=float(z_numerator/z_sum)
            center_leucin=[x_center, y_center, z_center]
            print('leucin')
            print(center_leucin)
    elif aminoacid_name=='VAL':
        if atom_name=='N  ':
            xN=float(line[31:38])
            yN=float(line[39:46])
            zN=float(line[47:54])
            N_koordinates=[xN, yN, zN]
            print(N_koordinates)
        if atom_name=='CA ':
            xCA=float(line[31:38])
            yCA=float(line[39:46])
            zCA=float(line[47:54])
            CA_koordinates=[xCA, yCA, zCA]
            print(CA_koordinates)
        if atom_name=='C  ':
            xC=float(line[31:38])
            yC=float(line[39:46])
            zC=float(line[47:54])
            C_koordinates=[xC, yC, zC]
            print(C_koordinates)
        if atom_name=='O  ':
            xO=float(line[31:38])
            yO=float(line[39:46])
            zO=float(line[47:54])
            O_koordinates=[xO, yO, zO]
            print(O_koordinates)
        if atom_name=='CB ':
            xCB=float(line[31:38])
            yCB=float(line[39:46])
            zCB=float(line[47:54])
            CB_koordinates=[xCB, yCB, zCB]
            print(CB_koordinates)
        if atom_name=='CG1':
            xCG1=float(line[31:38])
            yCG1=float(line[39:46])
            zCG1=float(line[47:54])
            CG1_koordinates=[xCG1, yCG1, zCG1]
            print(CG1_koordinates)
        if atom_name=='CG2':
            xCG2=float(line[31:38])
            yCG2=float(line[39:46])
            zCG2=float(line[47:54])
            CG2_koordinates=[xCG2, yCG2, zCG2]
            print(CG2_koordinates)
            x_sum=xN+xCA+xC+xO+xCB+xCG1+xCG2
            x_numerator=(xCA+xC+xCB+xCG1+xCG2)*12+xN*14+xO*16
            x_center=float(x_numerator/x_sum)
            y_sum=yN+yCA+yO+yCB+yCG1+yCG2+yC
            y_numerator=(yCA+yCB+yCG1+yCG2+yC)*12+yN*14+yO*16
            y_center=float(y_numerator/y_sum)
            z_sum=zN+zCA+zO+zCB+zCG1+zCG2+zC
            z_numerator=(zCA+zCB+zCG1+zCG2+zC)*12+zN*14+zO*16
            z_center=float(z_numerator/z_sum)
            center_valin = [x_center, y_center, z_center]
            print('valin')
            print(center_valin)
    elif aminoacid_name=='TRP':
        if atom_name=='N  ':
            xN=float(line[31:38])
            yN=float(line[39:46])
            zN=float(line[47:54])
            N_koordinates=[xN, yN, zN]
            print(N_koordinates)
        if atom_name=='CA ':
            xCA=float(line[31:38])
            yCA=float(line[39:46])
            zCA=float(line[47:54])
            CA_koordinates=[xCA, yCA, zCA]
            print(CA_koordinates)
        if atom_name=='C  ':
            xC=float(line[31:38])
            yC=float(line[39:46])
            zC=float(line[47:54])
            C_koordinates=[xC, yC, zC]
            print(C_koordinates)
        if atom_name=='O  ':
            xO=float(line[31:38])
            yO=float(line[39:46])
            zO=float(line[47:54])
            O_koordinates=[xO, yO, zO]
            print(O_koordinates)
        if atom_name=='CB ':
            xCB=float(line[31:38])
            yCB=float(line[39:46])
            zCB=float(line[47:54])
            CB_koordinates=[xCB, yCB, zCB]
            print(CB_koordinates)
        if atom_name=='CG ':
            xCG=float(line[31:38])
            yCG=float(line[39:46])
            zCG=float(line[47:54])
            CG_koordinates=[xCG, yCG, zCG]
            print(CG_koordinates)
        if atom_name=='CD1':
            xCD1=float(line[31:38])
            yCD1=float(line[39:46])
            zCD1=float(line[47:54])
            CD1_koordinates=[xCD1, yCD1, zCD1]
            print(CD1_koordinates)
        if atom_name=='CD2':
            xCD2=float(line[31:38])
            yCD2=float(line[39:46])
            zCD2=float(line[47:54])
            CD2_koordinates=[xCD2, yCD2, zCD2]
            print(CD2_koordinates)
        if atom_name=='CE2':
            xCE2=float(line[31:38])
            yCE2=float(line[39:46])
            zCE2=float(line[47:54])
            CE2_koordinates=[xCE2, yCE2, zCE2]
            print(CE2_koordinates)
        if atom_name=='CE3':
            xCE3=float(line[31:38])
            yCE3=float(line[39:46])
            zCE3=float(line[47:54])
            CE3_koordinates=[xCE3, yCE3, zCE3]
            print(CE3_koordinates)
        if atom_name=='NE1':
            xNE1=float(line[31:38])
            yNE1=float(line[39:46])
            zNE1=float(line[47:54])
            NE1_koordinates=[xNE1, yNE1, zNE1]
            print(NE1_koordinates)        
        if atom_name=='CZ2':
            xCZ2=float(line[31:38])
            yCZ2=float(line[39:46])
            zCZ2=float(line[47:54])
            CZ2_koordinates=[xCZ2, yCZ2, zCZ2]
            print(CZ2_koordinates)
        if atom_name=='CZ3':
            xCZ3=float(line[31:38])
            yCZ3=float(line[39:46])
            zCZ3=float(line[47:54])
            CZ3_koordinates=[xCZ3, yCZ3, zCZ3]
            print(CZ3_koordinates)
        if atom_name=='CH2':
            xCH2=float(line[31:38])
            yCH2=float(line[39:46])
            zCH2=float(line[47:54])
            CH2_koordinates=[xCH2, yCH2, zCH2]
            print(CH2_koordinates)
            x_sum=xN+xCA+xC+xO+xCB+xCG+xCD1+xCD2+xCE2+xCE3+xNE1+xCZ2+xCZ3+xCH2
            x_numerator=(xCA+xCB+xC+xCG+xCD1+xCD2+xCE2+xCE3+xCZ2+xCZ3+xCH2)*12+(xN+xNE1)*14+xO*16
            x_center=float(x_numerator/x_sum)
            y_sum=yN+yCA+yC+yO+yCB+yCG+yCD1+yCD2+yCE2+yCE3+yNE1+yCZ2+yCZ3+yCH2
            y_numerator=(yCA+yCB+yC+yCG+yCD1+yCD2+yCE2+yCE3+yCZ2+yCZ3+yCH2)*12+(yN+yNE1)*14+yO*16
            y_center=float(y_numerator/y_sum)
            z_sum=zN+zCA+zC+zO+zCB+zCG+zCD1+zCD2+zCE2+zCE3+zNE1+zCZ2+zCZ3+zCH2
            z_numerator=(zCA+zCB+zC+zCG+zCD1+zCD2+zCE2+zCE3+zCZ2+zCZ3+zCH2)*12+(zN+zNE1)*14+zO*16
            z_center=float(z_numerator/z_sum)
            center_tryptophan = [x_center, y_center, z_center]
            print('triptophan')
            print(center_tryptophan)
    elif aminoacid_name=='PHE':
        if atom_name=='N  ':
            xN=float(line[31:38])
            yN=float(line[39:46])
            zN=float(line[47:54])
            N_koordinates=[xN, yN, zN]
            print(N_koordinates)
        if atom_name=='CA ':
            xCA=float(line[31:38])
            yCA=float(line[39:46])
            zCA=float(line[47:54])
            CA_koordinates=[xCA, yCA, zCA]
            print(CA_koordinates)
        if atom_name=='C  ':
            xC=float(line[31:38])
            yC=float(line[39:46])
            zC=float(line[47:54])
            C_koordinates=[xC, yC, zC]
            print(C_koordinates)
        if atom_name=='O  ':
            xO=float(line[31:38])
            yO=float(line[39:46])
            zO=float(line[47:54])
            O_koordinates=[xO, yO, zO]
            print(O_koordinates)
        if atom_name=='CB ':
            xCB=float(line[31:38])
            yCB=float(line[39:46])
            zCB=float(line[47:54])
            CB_koordinates=[xCB, yCB, zCB]
            print(CB_koordinates)
        if atom_name=='CG ':
            xCG=float(line[31:38])
            yCG=float(line[39:46])
            zCG=float(line[47:54])
            CG_koordinates=[xCG, yCG, zCG]
            print(CG_koordinates)
        if atom_name=='CD1':
            xCD1=float(line[31:38])
            yCD1=float(line[39:46])
            zCD1=float(line[47:54])
            CD1_koordinates=[xCD1, yCD1, zCD1]
            print(CD1_koordinates)
        if atom_name=='CD2':
            xCD2=float(line[31:38])
            yCD2=float(line[39:46])
            zCD2=float(line[47:54])
            CD2_koordinates=[xCD2, yCD2, zCD2]
            print(CD2_koordinates)
        if atom_name=='CE1':
            xCE1=float(line[31:38])
            yCE1=float(line[39:46])
            zCE1=float(line[47:54])
            CE1_koordinates=[xCE1, yCE1, zCE1]
            print(CE1_koordinates)
        if atom_name=='CE2':
            xCE2=float(line[31:38])
            yCE2=float(line[39:46])
            zCE2=float(line[47:54])
            CE2_koordinates=[xCE2, yCE2, zCE2]
            print(CE2_koordinates)
        if atom_name=='CZ':
            xCZ=float(line[31:38])
            yCZ=float(line[39:46])
            zCZ=float(line[47:54])
            CZ_koordinates=[xCZ, yCZ, zCZ]
            print(CZ_koordinates)
            x_sum=xN+xCA+xC+xO+xCB+xCG+xCD1+xCD2+xCE1+xCE2+xCZ
            x_numerator=(xCA+xCB+xCG+xCD1+xCD2+xCE1+xCE2+xCZ+xC)*12+xN*14+xO*16
            x_center=float(x_numerator/x_sum)
            y_sum=yN+yCA+yO+yCB+yCG+yCD1+yCD2+yCE1+yCE2+yCZ+yC
            y_numerator=(yCA+yCB+yC+yCG+yCD1+yCD2+yCE1+yCE2+yCZ)*12+yN*14+yO*16
            y_center=float(y_numerator/y_sum)
            z_sum=zN+zCA+zC+zO+zCB+zCG+zCD1+zCD2+zCE1+zCE2+zCZ
            z_numerator=(zCA+zCB+zC+zCG+zCD1+zCD2+zCE1+zCE2+zCZ)*12+zN*14+zO*16
            z_center=float(z_numerator/z_sum)
            center_phenylalanine = [x_center, y_center, z_center]
            print('phenylalanine')
            print(center_phenylalanine)
    elif aminoacid_name == 'MET':
        if atom_name=='N  ':
            xN=float(line[31:38])
            yN=float(line[39:46])
            zN=float(line[47:54])
            N_koordinates=[xN, yN, zN]
            print(N_koordinates)
        if atom_name=='CA ':
            xCA=float(line[31:38])
            yCA=float(line[39:46])
            zCA=float(line[47:54])
            CA_koordinates=[xCA, yCA, zCA]
            print(CA_koordinates)
        if atom_name=='C  ':
            xC=float(line[31:38])
            yC=float(line[39:46])
            zC=float(line[47:54])
            C_koordinates=[xC, yC, zC]
            print(C_koordinates)
        if atom_name=='O  ':
            xO=float(line[31:38])
            yO=float(line[39:46])
            zO=float(line[47:54])
            O_koordinates=[xO, yO, zO]
        if atom_name=='CB ':
            xCB=float(line[31:38])
            yCB=float(line[39:46])
            zCB=float(line[47:54])
            CB_koordinates=[xCB, yCB, zCB]
            print(CB_koordinates)
        if atom_name=='CG ':
            xCG=float(line[31:38])
            yCG=float(line[39:46])
            zCG=float(line[47:54])
            CG_koordinates=[xCG, yCG, zCG]
            print(CG_koordinates)
        if atom_name=='SD ':
            xSD=float(line[31:38])
            ySD=float(line[39:46])
            zSD=float(line[47:54])
            SD_koordinates=[xSD, ySD, zSD]
            print(SD_koordinates)
        if atom_name=='CE':
            xCE=float(line[31:38])
            yCE=float(line[39:46])
            zCE=float(line[47:54])
            CE_koordinates=[xCE, yCE, zCE]
            print(CE_koordinates)
            x_sum=xN+xCA+xC+xO+xCB+xCG+xCE+xSD
            x_numerator=(xCA+xCB+xCG+xCE+xC)*12+xN*14+xO*16+xSD*32
            x_center=float(x_numerator/x_sum)
            y_sum=yN+yCA+yO+yCB+yCG+xCE+xSD+xC
            y_numerator=(yCA+yCB+yC+yCG+yCE)*12+yN*14+yO*16+ySD*32
            y_center=float(y_numerator/y_sum)
            z_sum=zN+zCA+zC+zO+zCB+zCG+zCE+zSD
            z_numerator=(zCA+zCB+zC+zCG+zCE+zSD)*12+zN*14+zO*16+zSD*32
            z_center=float(z_numerator/z_sum)
            center_methionine = [x_center, y_center, z_center]
            print('methionine')
            print(center_methionine)
    elif aminoacid_name == 'ALA':
        if atom_name=='N  ':
            xN=float(line[31:38])
            yN=float(line[39:46])
            zN=float(line[47:54])
            N_koordinates=[xN, yN, zN]
            print(N_koordinates)
        if atom_name=='CA ':
            xCA=float(line[31:38])
            yCA=float(line[39:46])
            zCA=float(line[47:54])
            CA_koordinates=[xCA, yCA, zCA]
            print(CA_koordinates)
        if atom_name=='C  ':
            xC=float(line[31:38])
            yC=float(line[39:46])
            zC=float(line[47:54])
            C_koordinates=[xC, yC, zC]
            print(C_koordinates)
        if atom_name=='O  ':
            xO=float(line[31:38])
            yO=float(line[39:46])
            zO=float(line[47:54])
            O_koordinates=[xO, yO, zO]
            print(O_koordinates)
        if atom_name=='CB ':
            xCB=float(line[31:38])
            yCB=float(line[39:46])
            zCB=float(line[47:54])
            CB_koordinates=[xCB, yCB, zCB]
            print(CB_koordinates)
            x_sum=xN+xCA+xC+xO+xCB
            x_numerator=(xCA+xC+xCB)*12+xN*14+xO*16
            x_center=float(x_numerator/x_sum)
            y_sum=yN+yCA+yO+yCB+yC
            y_numerator=(yCA+yCB+yC)*12+yN*14+yO*16
            y_center=float(y_numerator/y_sum)
            z_sum=zN+zCA+zO+zC+zCB
            z_numerator=(zCA+zCB+zC)*12+zN*14+zO*16
            z_center=float(z_numerator/z_sum)
            center_alanine = [x_center, y_center, z_center]
            print('alanine')
            print(center_alanine)
    elif aminoacid_name == 'ILE':
        if atom_name=='N  ':
            xN=float(line[31:38])
            yN=float(line[39:46])
            zN=float(line[47:54])
            N_koordinates=[xN, yN, zN]
            print(N_koordinates)
        if atom_name=='CA ':
            xCA=float(line[31:38])
            yCA=float(line[39:46])
            zCA=float(line[47:54])
            CA_koordinates=[xCA, yCA, zCA]
            print(CA_koordinates)
        if atom_name=='C  ':
            xC=float(line[31:38])
            yC=float(line[39:46])
            zC=float(line[47:54])
            C_koordinates=[xC, yC, zC]
            print(C_koordinates)
        if atom_name=='O  ':
            xO=float(line[31:38])
            yO=float(line[39:46])
            zO=float(line[47:54])
            O_koordinates=[xO, yO, zO]
            print(O_koordinates)
        if atom_name=='CB ':
            xCB=float(line[31:38])
            yCB=float(line[39:46])
            zCB=float(line[47:54])
            CB_koordinates=[xCB, yCB, zCB]
            print(CB_koordinates)
        if atom_name=='CG1':
            xCG1=float(line[31:38])
            yCG1=float(line[39:46])
            zCG1=float(line[47:54])
            CG1_koordinates=[xCG1, yCG1, zCG1]
            print(CG1_koordinates)
        if atom_name=='CG2':
            xCG2=float(line[31:38])
            yCG2=float(line[39:46])
            zCG2=float(line[47:54])
            CG2_koordinates=[xCG2, yCG2, zCG2]
            print(CG2_koordinates)
        if atom_name=='CD1':
            xCD1=float(line[31:38])
            yCD1=float(line[39:46])
            zCD1=float(line[47:54])
            CD1_koordinates=[xCD1, yCD1, zCD1]
            print(CD1_koordinates)
            x_sum=xN+xCA+xC+xO+xCB+xCG1+xCG2+xCD1
            x_numerator=(xCA+xC+xCB+xCG1+xCG2+xCD1)*12+xN*14+xO*16
            x_center=float(x_numerator/x_sum)
            y_sum=yN+yCA+yO+yCB+yC+yCG1+yCG2+yCD1
            y_numerator=(yCA+yCB+yC+yCG1+yCG2+yCD1)*12+yN*14+yO*16
            y_center=float(y_numerator/y_sum)
            z_sum=zN+zCA+zO+zC+zCB+zCG1+zCG2+zCD1
            z_numerator=(zCA+zCB+zC+zCG1+zCG2+zCD1)*12+zN*14+zO*16
            z_center=float(z_numerator/z_sum)
            center_isoleucine = [x_center, y_center, z_center]
            print('isoleucine')
            print(center_isoleucine)
    elif aminoacid_name == 'GLY':
        if atom_name=='N  ':
            xN=float(line[31:38])
            yN=float(line[39:46])
            zN=float(line[47:54])
            N_koordinates=[xN, yN, zN]
            print(N_koordinates)
        if atom_name=='CA ':
            xCA=float(line[31:38])
            yCA=float(line[39:46])
            zCA=float(line[47:54])
            CA_koordinates=[xCA, yCA, zCA]
            print(CA_koordinates)
        if atom_name=='C  ':
            xC=float(line[31:38])
            yC=float(line[39:46])
            zC=float(line[47:54])
            C_koordinates=[xC, yC, zC]
            print(C_koordinates)
        if atom_name=='O  ':
            xO=float(line[31:38])
            yO=float(line[39:46])
            zO=float(line[47:54])
            O_koordinates=[xO, yO, zO]
            print(O_koordinates)
            x_sum=xN+xCA+xC+xO
            x_numerator=(xCA+xC)*12+xN*14+xO*16
            x_center=float(x_numerator/x_sum)
            y_sum=yN+yCA+yO+yC
            y_numerator=(yCA+yC)*12+yN*14+yO*16
            y_center=float(y_numerator/y_sum)
            z_sum=zN+zCA+zO+zC
            z_numerator=(zCA+zC)*12+zN*14+zO*16
            z_center=float(z_numerator/z_sum)
            center_glycine = [x_center, y_center, z_center]
            print('glycine')
            print(center_glycine)
    elif aminoacid_name == 'PRO':
        if atom_name=='N  ':
            xN=float(line[31:38])
            yN=float(line[39:46])
            zN=float(line[47:54])
            N_koordinates=[xN, yN, zN]
            print(N_koordinates)
        if atom_name=='CA ':
            xCA=float(line[31:38])
            yCA=float(line[39:46])
            zCA=float(line[47:54])
            CA_koordinates=[xCA, yCA, zCA]
            print(CA_koordinates)
        if atom_name=='C  ':
            xC=float(line[31:38])
            yC=float(line[39:46])
            zC=float(line[47:54])
            C_koordinates=[xC, yC, zC]
            print(C_koordinates)
        if atom_name=='O  ':
            xO=float(line[31:38])
            yO=float(line[39:46])
            zO=float(line[47:54])
            O_koordinates=[xO, yO, zO]
            print(O_koordinates)
        if atom_name=='CB ':
            xCB=float(line[31:38])
            yCB=float(line[39:46])
            zCB=float(line[47:54])
            CB_koordinates=[xCB, yCB, zCB]
            print(CB_koordinates)
        if atom_name=='CG ':
            xCG=float(line[31:38])
            yCG=float(line[39:46])
            zCG=float(line[47:54])
            CG_koordinates=[xCG, yCG, zCG]
            print(CG_koordinates)
        if atom_name=='CD ':
            xCD=float(line[31:38])
            yCD=float(line[39:46])
            zCD=float(line[47:54])
            CD_koordinates=[xCD, yCD, zCD]
            print(CD_koordinates)
            x_sum=xN+xCA+xC+xO+xCB+xCG+xCD
            x_numerator=(xCA+xCB+xCG+xC+xCD)*12+xN*14+xO*16
            x_center=float(x_numerator/x_sum)
            y_sum=yN+yCA+yO+yCB+yCG+xCD+xC
            y_numerator=(yCA+yCB+yC+yCG+yCD)*12+yN*14+yO*16
            y_center=float(y_numerator/y_sum)
            z_sum=zN+zCA+zC+zO+zCB+zCG+zCD
            z_numerator=(zCA+zCB+zC+zCG+zCD)*12+zN*14+zO*16
            z_center=float(z_numerator/z_sum)
            center_proline = [x_center, y_center, z_center]
            print('proline')
            print(center_proline)