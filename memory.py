def stage_1(array):
    if array[4] == 1:
        return 1
    elif array[4] == 2:
        return 1
    elif array[4] == 3:
        return 2
    elif array[4] == 4:
        return 3

def stage_2(array, stage_1_ind):
    if array[4] == 1:
        return array.index(4)
    elif array[4] == 2:
        return stage_1_ind
    elif array[4] == 3:
        return 0
    elif array[4] == 4:
        return stage_1_ind

def stage_3(array, stage_1_label, stage_2_label):
    if array[4] == 1:
        return array.index(stage_2_label)
    elif array[4] == 2:
        return array.index(stage_1_label)
    elif array[4] == 3:
        return 2
    elif array[4] == 4:
        return array.index(4)

def stage_4(array, stage_1_ind, stage_2_ind):
    if array[4] == 1:
        return stage_1_ind
    elif array[4] == 2:
        return 0
    elif array[4] == 3:
        return stage_2_ind
    elif array[4] == 4:
        return stage_2_ind

def stage_5(array, stage_1_ind, stage_2_ind, stage_3_ind, stage_4_ind):
    if array[4] == 1:
        return stage_1_ind
    elif array[4] == 2:
        return stage_2_ind
    elif array[4] == 3:
        return stage_3_ind
    elif array[4] == 4:
        return stage_4_ind

code = \
[[1,3,2,4,1],
 [3,1,2,4,3],
 [2,3,4,1,2],
 [2,1,4,3,1],
 [4,1,2,3,4]]

stage_1_ind = stage_1(code[0])
stage_1_lab = code[0][stage_1_ind]
stage_2_ind = stage_2(code[1], stage_1_ind)
stage_2_lab = code[1][stage_2_ind]
stage_3_ind = stage_3(code[2], stage_1_lab, stage_2_lab)
stage_3_lab = code[2][stage_3_ind]
stage_4_ind = stage_4(code[3], stage_1_ind, stage_2_ind)
stage_4_lab = code[3][stage_4_ind]
stage_5_ind = stage_5(code[4], stage_1_ind, stage_2_ind, stage_3_ind, stage_4_ind)
stage_5_lab = code[4][stage_5_ind]
print(f"{stage_1_lab}{stage_2_lab}{stage_3_lab}{stage_4_lab}{stage_5_lab}")
