#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 12:34:04 2023

@author: mark hunnell wssu 
"""
"""
min_rank_dict is a dictionary with all minimum ranks of graphs on at most 8 vertices.  First entry is a placeholder and does not correspond to a graph.
"""
min_rank_dict = {'?': None, '@': 0, 'A?': 0, 'A_': 1, 'B?': 0, 'BG': 1, 'BW': 2, 'Bw': 1, 'C?': 0, 'C@': 1, 'CB': 2, 'C`': 2, 'CJ': 1, 'CF': 2, 'CR': 3, 'CN': 2, 'Cr': 2, 'C^': 2, 'C~': 1, 'D??': 0, 'D?C': 1, 'D?K': 2, 'DGC': 2, 'D@K': 1, 'D?[': 2, 'DAK': 3, 'D_K': 3, 'D@[': 2, 'DIK': 2, 'D?{': 2, 'DC[': 3, 'DDW': 4, 'D`K': 2, 'DB[': 2, 'D@{': 3, 'DD[': 3, 'DK[': 3, 'DIk': 3, 'DqK': 3, 'DJ[': 1, 'DB{': 3, 'DR[': 3, 'D`{': 2, 'DMk': 3, 'DFw': 2, 'DJ{': 2, 'DF{': 2, 'DR{': 3, 'DNw': 2, 'DN{': 2, 'Dr{': 2, 'D^{': 2, 'D~{': 1, 'E???': 0, 'E??G': 1, 'E@?G': 2, 'E??W': 2, 'E?CW': 1, 'E??w': 2, 'E?GW': 3, 'EG?W': 3, 'E`?G': 3, 'E?Cw': 2, 'E@GW': 2, 'E?@w': 2, 'E?Ow': 3, 'E?So': 4, 'EGCW': 2, 'E_?w': 3, 'E@`G': 4, 'E?oo': 4, 'E?Kw': 2, 'E?Dw': 3, 'E?Sw': 3, 'E@Ow': 3, 'E@HW': 3, 'EIGW': 3, 'E?Bw': 2, 'E?`w': 3, 'E?ow': 4, 'ECOw': 4, 'ECDg': 4, 'E_Cw': 3, 'E@hO': 5, 'E@N?': 3, 'E`GW': 3, 'E@Kw': 1, 'E?Lw': 3, 'EAKw': 3, 'EGDw': 2, 'E@XW': 3, 'E?\\o': 2, 'E?Fw': 3, 'E?dw': 4, 'ECSw': 4, 'E@`w': 4, 'E@JW': 4, 'ECLg': 4, 'E@hW': 4, 'E?lo': 4, 'E@NG': 3, 'E_Kw': 3, 'E`Ow': 4, 'EI_w': 4, 'EIIW': 4, 'EqGW': 4, 'EwCW': 2, 'E@Lw': 2, 'E?\\w': 2, 'EALw': 3, 'E@\\o': 2, 'E?Nw': 4, 'E?lw': 4, 'ECLw': 4, 'E@NW': 3, 'E@lo': 4, 'E`Kw': 2, 'EGFw': 3, 'EGUw': 4, 'EGdw': 3, 'E_Lw': 4, 'E?^o': 3, 'EBUg': 4, 'EQSw': 4, 'EIMW': 4, 'EBYW': 3, 'EK`w': 3, 'EBqg': 4, 'E`hW': 4, 'E@zO': 3, 'E`ow': 3, 'E@\\w': 2, 'EILw': 2, 'E@Nw': 3, 'E@lw': 3, 'E?^w': 3, 'EANw': 4, 'E@tw': 4, 'EC\\w': 3, 'EPTw': 4, 'EBYw': 3, 'EHNW': 3, 'E`Lw': 3, 'EJYW': 3, 'E_Nw': 3, 'E@zW': 3, 'E?~o': 2, 'EQdw': 4, 'EEhw': 4, 'EENg': 3, 'EKdw': 3, 'ED^_': 3, 'ETXW': 4, 'E`lo': 3, 'ELhW': 3, 'EB\\w': 2, 'E@^w': 3, 'ED\\w': 3, 'EINw': 3, 'EI]w': 3, 'EK\\w': 3, 'E?~w': 2, 'EC^w': 3, 'EElw': 3, 'EDZw': 4, 'E`Nw': 2, 'EBng': 3, 'EQlw': 4, 'EImw': 3, 'E`lw': 3, 'E@~o': 3, 'EMhw': 3, 'EJqw': 3, 'EbYw': 3, 'Erow': 3, 'E]ow': 2, 'EJ\\w': 1, 'EB^w': 3, 'ER\\w': 3, 'E@~w': 3, 'ED^w': 3, 'ET\\w': 3, 'EInw': 3, 'EK^w': 3, 'EJuw': 3, 'ER^W': 3, 'EB~o': 3, 'EqNw': 3, 'ERzW': 3, 'EFzg': 2, 'E`~o': 2, 'EJ^w': 2, 'EB~w': 3, 'ER^w': 3, 'EJ~o': 2, 'E`~w': 2, 'EMnw': 3, 'EFzw': 2, 'ER~o': 3, 'Et\\w': 2, 'EJ~w': 2, 'EF~w': 2, 'ER~w': 3, 'ENzw': 2, 'E}lw': 2, 'EN~w': 2, 'Er~w': 2, 'E^~w': 2, 'E~~w': 1, 'F????': 0, 'F???G': 1, 'F???W': 2, 'F?C?G': 2, 'F??GW': 1, 'F???w': 2, 'F??OW': 3, 'F@??W': 3, 'FGC?G': 3, 'F??Gw': 2, 'F?COW': 2, 'F??@w': 2, 'F??_w': 3, 'F??go': 4, 'F@?GW': 2, 'FG??w': 3, 'F?D@G': 4, 'F?@_o': 4, 'F`??W': 4, 'F??Ww': 2, 'F??Hw': 3, 'F??gw': 3, 'F?C_w': 3, 'F?CPW': 3, 'F@GOW': 3, 'F??Bw': 2, 'F?@@w': 3, 'F?@_w': 4, 'F?OHg': 4, 'F?O_w': 4, 'FG?Gw': 3, 'F?DPO': 5, 'F?CZ?': 3, 'FGCOW': 3, 'F_?@w': 3, 'F_?_w': 4, 'F?B@o': 4, 'F@AIO': 5, 'F?`H_': 5, 'F`?GW': 3, 'F?CWw': 1, 'F??Xw': 3, 'F?GWw': 3, 'F@?Hw': 2, 'F?CpW': 3, 'F??xo': 2, 'F??Jw': 3, 'F?@Hw': 4, 'F?Ogw': 4, 'F?D@w': 4, 'F?CRW': 4, 'F?OXg': 4, 'F?DPW': 4, 'F?CZG': 3, 'F?@Xo': 4, 'FG?Ww': 3, 'FGC_w': 4, 'F@H?w': 4, 'F@GQW': 4, 'FIGOW': 4, 'FJ?GW': 2, 'F??Fw': 2, 'F?ABw': 3, 'F?B@w': 4, 'F?`@w': 4, 'F?_Jg': 4, 'F_?Hw': 4, 'F?F@W': 5, 'F@AIW': 4, 'F?BHo': 4, 'FCD@W': 5, 'FCCJG': 5, 'F_CPW': 4, 'FE?HW': 4, 'FGE?w': 4, 'FCO_w': 5, 'F?C^?': 3, 'F?Ma_': 6, 'F@MAG': 4, 'F@G]?': 4, 'F`GOW': 4, 'F?CXw': 2, 'F??xw': 2, 'F?GXw': 3, 'F?Cxo': 2, 'F??Zw': 4, 'F?@Xw': 4, 'F?OXw': 4, 'F?CZW': 3, 'F?DXo': 4, 'FGCWw': 2, 'F@?Jw': 3, 'F@?iw': 4, 'F@@Hw': 3, 'FG?Xw': 4, 'F??zo': 3, 'F?Kig': 4, 'F@GYW': 4, 'FAGgw': 4, 'F?KqW': 3, 'F@P@w': 3, 'F?Lag': 4, 'F?DrO': 3, 'FGDPW': 4, 'FGD_w': 3, 'F??Nw': 3, 'F?AJw': 4, 'F?BHw': 4, 'F?`Hw': 5, 'F?EBw': 4, 'F?CVW': 4, 'FC@Hw': 5, 'FC?ZW': 5, 'F?ERW': 5, 'F_?Xw': 4, 'F?F@w': 4, 'F?AZo': 4, 'F?C^G': 3, 'F?IYo': 5, 'F@`Gw': 5, 'F?oXg': 4, 'FG_Ww': 4, 'FOCaw': 5, 'F@IAw': 5, 'F@`@w': 5, 'F@GUW': 5, 'F`?Hw': 3, 'F?gqg': 5, 'F@_ig': 5, 'FCOpW': 5, 'F@_qW': 4, 'F?Mag': 5, 'F?_z_': 5, 'F?ErO': 5, 'F@?}O': 4, 'F?KuG': 4, 'F_CpW': 4, 'F?opg': 4, 'F_?xo': 3, 'FBOcW': 5, 'FWD?w': 5, 'FQO_w': 5, 'FII?w': 5, 'FJ?KW': 3, 'FqGOW': 5, 'Fr?GW': 3, 'F?Cxw': 2, 'F@GXw': 2, 'F?CZw': 3, 'F?DXw': 3, 'F??zw': 3, 'F?GZw': 4, 'F?Dhw': 4, 'F?Oxw': 3, 'FAChw': 4, 'F?Kqw': 3, 'F@CZW': 3, 'FGCXw': 3, 'F@KqW': 3, 'FG?Zw': 3, 'F?DrW': 3, 'F?@zo': 2, 'FAHHw': 4, 'F?XPw': 4, 'F?WZg': 3, 'F@PHw': 3, 'F?Sz_': 3, 'FGDXo': 3, 'FASpW': 4, 'F@TPW': 3, 'F??^w': 4, 'F?AZw': 4, 'F?_Zw': 5, 'F?C^W': 3, 'F?IYw': 5, 'F?FHw': 4, 'F?dPw': 5, 'FCCZW': 4, 'F_CXw': 3, 'F@?Nw': 4, 'F@AJw': 4, 'F@?mw': 5, 'FO?Zw': 5, 'F??~o': 4, 'F?ErW': 5, 'F?_zg': 5, 'F@?}W': 4, 'F?Azo': 4, 'F_?xw': 3, 'F@IIw': 5, 'FCHHw': 5, 'FOGYw': 5, 'F?gqw': 5, 'F?gZg': 5, 'FCGiw': 4, 'F?hPw': 4, 'F?MJg': 4, 'F?Kmg': 4, 'F_GXw': 4, 'F?N@w': 4, 'F@`Hw': 4, 'F@G]W': 4, 'F?KuW': 4, 'F?cz_': 5, 'FKCXW': 5, 'FCSpW': 5, 'F?spg': 4, 'FCOxo': 4, 'F_Cxo': 3, 'FWCWw': 3, 'F@PDw': 4, 'FGEBw': 4, 'FI?kw': 5, 'FK@Hw': 5, 'Fg?Xw': 5, 'F`@Hw': 4, 'FIAHw': 4, 'F@R@w': 4, 'FAHcw': 5, 'FG@\\o': 4, 'FGDcw': 4, 'FGAZo': 4, 'F_?zo': 4, 'FCXHg': 5, 'FAWkg': 5, 'FGSkg': 5, 'FDPHW': 5, 'FGW[g': 4, 'FBOkW': 5, 'F?X\\_': 5, 'FKOgw': 5, 'F@XSW': 4, 'F?\\cg': 4, 'FCX_w': 4, 'F``@w': 4, 'FSP@w': 4, 'F_Mag': 5, 'FANDG': 5, 'F_KuG': 4, 'F?Ne_': 4, 'FGFTO': 4, 'FGFco': 4, 'F@NEG': 3, 'F?Kxw': 2, 'F?Czw': 3, 'F?Sxw': 3, 'F@GZw': 3, 'F@Gyw': 3, 'F@Oxw': 3, 'F?@zw': 2, 'F?Ozw': 3, 'F?XXw': 3, 'F?Srw': 4, 'FGCZw': 2, 'F?LZg': 3, 'FAHXw': 4, 'F@HYw': 3, 'FGDXw': 3, 'F?Dzo': 3, 'F@XPw': 3, 'F@Law': 3, 'FGKqw': 3, 'FIL_w': 3, 'FBX_w': 2, 'F?C^w': 3, 'F?EZw': 4, 'F?dXw': 4, 'F??~w': 4, 'F?Azw': 4, 'F?G^w': 5, 'F?IZw': 5, 'F?_zw': 4, 'F?G}w': 4, 'F?Miw': 5, 'F?K}W': 4, 'FCCjw': 5, 'F@C^W': 4, 'F?Kuw': 4, 'FOCZw': 4, 'FAIXw': 5, 'F?czg': 5, 'F?MZg': 4, 'FGEXw': 4, 'F?NPw': 4, 'F@IYw': 4, 'FCOxw': 4, 'F?Ezo': 4, 'F_Cxw': 3, 'F@hPw': 5, 'FOKqw': 4, 'F@Maw': 4, 'F@KuW': 4, 'F@N@w': 3, 'F`GXw': 3, 'FG?^w': 4, 'FG@\\w': 4, 'FGAZw': 4, 'F_?zw': 4, 'F?@~o': 3, 'FAHLw': 5, 'FCOjw': 5, 'F@QJw': 4, 'F?YRw': 4, 'F?XTw': 5, 'F?W^g': 4, 'F@PLw': 4, 'F_Dhw': 5, 'F@FJW': 5, 'FGFHw': 5, 'F?Naw': 5, 'F@`iw': 4, 'F?drW': 4, 'FGDkw': 4, 'F?LuW': 4, 'F?Fjo': 4, 'FCDjW': 4, 'F?`zo': 3, 'FaChw': 5, 'FEOhw': 5, 'FECjW': 5, 'FIEHw': 5, 'FAd`w': 5, 'FBDLW': 4, 'F@URW': 4, 'FAStW': 5, 'FOTPw': 4, 'FGSsw': 4, 'FAU`w': 4, 'FQCZW': 4, 'FIC\\W': 4, 'FALcw': 4, 'FBEJW': 4, 'FCSrW': 4, 'F@TTW': 4, 'FAK^G': 4, 'FKCZW': 4, 'FgCXw': 4, 'F@drO': 4, 'F@LuO': 4, 'F@lag': 5, 'F`KqW': 4, 'F?lr_': 4, 'F`?Nw': 3, 'FKAJw': 4, 'Fo?Zw': 4, 'F_?~o': 3, 'FGFTW': 4, 'F?Neg': 4, 'FGFcw': 3, 'F?FvO': 3, 'FcHHw': 5, 'FOoZg': 4, 'FAj@w': 5, 'FGeJg': 4, 'F_hPw': 5, 'F?yRg': 4, 'FCYJg': 4, 'FQ`Hw': 5, 'F_N@w': 4, 'FSPHw': 4, 'F``Hw': 4, 'F@r@w': 3, 'F?o~_': 4, 'FGd\\_': 4, 'FAMuO': 4, 'FIMSW': 5, 'FANTO': 5, 'FGeZ_': 4, 'FWEYo': 4, 'FII[o': 4, 'F@NUO': 4, 'FCS~?': 4, 'F?ur_': 4, 'FwCWw': 2, 'F@Kxw': 1, 'F?Kzw': 3, 'FAKxw': 3, 'F?Dzw': 3, 'F?Szw': 3, 'FASxw': 3, 'F@Ozw': 3, 'F@HZw': 3, 'FAKzW': 3, 'F@Liw': 3, 'F?Lzo': 3, 'FIGZw': 3, 'FALrW': 3, 'F?\\rg': 2, 'FGDzo': 2, 'F?C~w': 4, 'F?Ezw': 4, 'F?czw': 4, 'F?K}w': 4, 'FCSxw': 4, 'F@G^w': 4, 'F@IZw': 4, 'F@_zw': 4, 'F@G}w': 4, 'F@Miw': 4, 'FCKzW': 4, 'F?Mzo': 4, 'F@K}W': 3, 'F_Kxw': 3, 'F?@~w': 3, 'F?O~w': 4, 'F?Fjw': 4, 'F?`zw': 3, 'F?YZw': 4, 'F?X\\w': 4, 'F?Svw': 5, 'FGC^w': 3, 'FAC~W': 4, 'FA_zw': 4, 'FAH\\w': 5, 'FAEjw': 5, 'FADlw': 4, 'F_Czw': 4, 'FGD\\w': 4, 'FAIZw': 4, 'FCDjw': 4, 'FAO|w': 4, 'FGEZw': 3, 'F?D~o': 4, 'F@pXw': 5, 'F@X[w': 4, 'F?\\\\g': 4, 'F@hYw': 4, 'FOTXw': 4, 'FGS{w': 4, 'FCXXw': 4, 'F?\\sw': 4, 'FPDJw': 5, 'FGKuw': 4, 'F@XTw': 4, 'F@Lew': 4, 'F@NBw': 3, 'F`GZw': 4, 'FPOyw': 5, 'FOSzg': 4, 'FBO|W': 4, 'F@drW': 4, 'F@W}g': 4, 'F@Ujg': 4, 'F@Yqw': 4, 'F@ozg': 4, 'F`Gyw': 4, 'F?]rg': 4, 'F@H}o': 4, 'F@LuW': 4, 'F@Qzo': 4, 'F`Oxw': 4, 'FQOxw': 4, 'F?lrg': 4, 'F@`zo': 4, 'F`XPw': 4, 'FBZ@w': 4, 'FJQHw': 4, 'FILcw': 4, 'FBXcw': 3, 'F_?~w': 3, 'F?FvW': 3, 'F?B~o': 2, 'F@`Nw': 4, 'F?ovw': 4, 'F_IZw': 4, 'F__zw': 4, 'FGaZw': 4, 'F?qrw': 4, 'F?o~g': 4, 'F?`~o': 3, 'F@h]W': 4, 'F?Nmo': 4, 'F@NMW': 3, 'FQEJw': 5, 'F@qRw': 5, 'FECnW': 4, 'F@dVW': 4, 'FGeRw': 3, 'FKC^W': 3, 'FBaJw': 4, 'FoCZw': 3, 'FH`[w': 5, 'FGU\\g': 4, 'FChZg': 4, 'FGd\\g': 4, 'FAiZg': 5, 'F?^Tg': 4, 'FGeZg': 4, 'FAM^G': 4, 'FCYZg': 4, 'FANTW': 4, 'FAMuW': 4, 'F?N^_': 4, 'FAJ\\o': 4, 'FII[w': 4, 'FWEYw': 4, 'FK`Xw': 4, 'F@NUW': 4, 'FGF\\o': 4, 'F@J]o': 4, 'FXEIw': 4, 'FTHIw': 5, 'FPdaw': 4, 'FHeaw': 4, 'FDLeW': 4, 'F`hPw': 4, 'FoKqw': 4, 'FPNAw': 4, 'FDZ@w': 4, 'F`Maw': 4, 'FRG]W': 4, 'FDhaw': 4, 'FFGmW': 3, 'FR`Hw': 4, 'FQKuW': 4, 'FTPHw': 4, 'F`KuW': 3, 'F`N@w': 3, 'F@^e_': 4, 'FB^DG': 4, 'FINco': 4, 'FIMuO': 3, 'F@Kzw': 2, 'F?Lzw': 3, 'FAKzw': 3, 'F@Lzo': 2, 'FGDzw': 2, 'F@XZw': 3, 'F?\\rw': 2, 'FALzo': 3, 'FISxw': 2, 'F?K~w': 4, 'F?Mzw': 4, 'FCKzw': 4, 'F@K}w': 3, 'F@Mzo': 4, 'F`Kxw': 2, 'F?D~w': 4, 'F?S~w': 4, 'F?NZw': 4, 'F?dzw': 4, 'FAS|w': 4, 'FAMZw': 4, 'F@H^w': 4, 'F@O~w': 4, 'F@H}w': 4, 'F@Qzw': 4, 'F@`zw': 4, 'F@W}w': 4, 'F@hZw': 4, 'FALlw': 4, 'FAgzw': 4, 'FOLZw': 4, 'F?[~g': 4, 'F@NJw': 4, 'FGK}w': 4, 'F?lrw': 4, 'F@X\\w': 4, 'F?\\tw': 4, 'F_Kzw': 4, 'FAkzg': 4, 'FEKzW': 4, 'FKSxw': 4, 'FCLzo': 4, 'FQSxw': 4, 'FaKxw': 4, 'FIG^w': 4, 'FHP\\w': 4, 'FIIZw': 4, 'F`Ozw': 4, 'FI_zw': 4, 'FIO|w': 3, 'FGD~o': 3, 'FG\\\\g': 4, 'FHX[w': 4, 'FKXXw': 4, 'FDXiw': 4, 'FBXkw': 3, 'FG\\sw': 3, 'FCXzo': 4, 'F?\\~_': 3, 'F?B~w': 2, 'F?`~w': 3, 'F?o~w': 4, 'F?Nmw': 4, 'FCDnw': 4, 'FCO~w': 4, 'F_C~w': 3, 'FAJ\\w': 4, 'F?N^g': 4, 'FGF\\w': 4, 'F@J]w': 4, 'F?F~o': 3, 'FOUZw': 4, 'FCozw': 4, 'F@qZw': 4, 'F?s~g': 4, 'FCYZw': 4, 'F?urw': 4, 'F@d^W': 4, 'FGeZw': 3, 'FAN\\o': 4, 'FIM[w': 4, 'F@N]o': 3, 'F@hVw': 5, 'F@NFw': 3, 'F`G^w': 3, 'FPDmw': 4, 'FDHmw': 4, 'FPFJw': 4, 'FPO}w': 4, 'FP`Zw': 4, 'FOUrw': 5, 'FPQZw': 4, 'FPH]w': 4, 'F@`~o': 4, 'F`_zw': 4, 'F@qrw': 4, 'FSOzw': 4, 'F`IZw': 4, 'F`G}w': 3, 'F@J^o': 4, 'F@New': 3, 'FWC}w': 3, 'F@lmg': 4, 'FAM~O': 4, 'FBMmW': 4, 'FAizo': 4, 'FBhkw': 4, 'FIMkw': 4, 'FKMiw': 4, 'FQMiw': 5, 'FEMjW': 4, 'FAY|o': 4, 'FBiiw': 4, 'FcKzW': 4, 'F`Miw': 4, 'F@Nmo': 3, 'F?l~_': 4, 'F@luW': 4, 'FQK}W': 4, 'F_Mzo': 4, 'F`K}W': 3, 'F`XTw': 4, 'FJQLw': 4, 'FBZDw': 4, 'FBqbw': 4, 'FJaJw': 3, 'FGttg': 4, 'FIdlg': 4, 'FBplg': 4, 'FHpsw': 4, 'FKhZg': 4, 'FANvO': 4, 'FGd~_': 3, 'F@^eg': 4, 'FIo|g': 3, 'FEhrW': 4, 'FI`|o': 4, 'FJ`kw': 4, 'FCxrg': 3, 'FINcw': 4, 'FKdrW': 4, 'FIMuW': 3, 'FK`zo': 3, 'F?^v_': 3, 'FdZ@w': 4, 'FRr@w': 3, 'Fr`Hw': 4, 'FtPHw': 3, 'F@Lzw': 2, 'F?\\zw': 2, 'FALzw': 3, 'F@\\rw': 2, 'FJXXw': 2, 'F@K~w': 3, 'F@Mzw': 3, 'F?L~w': 4, 'F?lzw': 4, 'FAK~w': 4, 'FAMzw': 4, 'FCLzw': 4, 'F@NZw': 4, 'FPLZw': 4, 'F@\\tw': 3, 'FHK}w': 3, 'F`Kzw': 3, 'FGD~w': 3, 'F@X^w': 4, 'F?\\vw': 3, 'FGL}w': 4, 'F_Lzw': 4, 'FGdzw': 3, 'F?^rw': 3, 'FBUjw': 4, 'FIMZw': 4, 'FQSzw': 4, 'FIS|w': 3, 'FBS~W': 4, 'FA\\tw': 4, 'FBYZw': 3, 'FDXzo': 4, 'F@\\~_': 3, 'F`Lzo': 3, 'F?F~w': 3, 'F?d~w': 4, 'F?uzw': 4, 'FCS~w': 4, 'FAN\\w': 4, 'F@N]w': 3, 'F@`~w': 4, 'F@J^w': 4, 'FCLnw': 4, 'F@h^w': 4, 'F?lvw': 4, 'F@NNw': 3, 'F_K~w': 3, 'FOUzw': 4, 'F@Vlw': 4, 'FAM~W': 4, 'F?^tw': 4, 'FGU|w': 4, 'F@qzw': 3, 'F@Nmw': 3, 'F_Mzw': 4, 'F?N~o': 4, 'FDNJw': 4, 'FDdjw': 4, 'FSLZw': 4, 'FBc~W': 4, 'FDhZw': 4, 'FKczw': 4, 'F@luw': 4, 'FKK}w': 4, 'FcKzw': 4, 'FEK~W': 3, 'F`K}w': 3, 'FDlrW': 4, 'F@l~_': 3, 'FBmrW': 3, 'F`Mzo': 3, 'F`O~w': 4, 'FII^w': 4, 'FI_~w': 4, 'FGd~g': 3, 'FI`|w': 4, 'FANvW': 4, 'FK`zw': 3, 'F?^vg': 3, 'FGF~o': 3, 'FKX\\w': 4, 'FAw~g': 4, 'FG^Tw': 4, 'FIY\\w': 4, 'FBZLw': 4, 'FaLlw': 4, 'FEYjw': 4, 'FKUjw': 4, 'FEXlw': 4, 'FBqjw': 4, 'F_[~g': 4, 'FG]^g': 3, 'FSXZw': 4, 'F`X\\w': 4, 'FC^bw': 3, 'F@zRw': 4, 'FINLw': 3, 'FKYZw': 4, 'F_\\tw': 3, 'F?|vg': 3, 'FI]\\g': 4, 'F@^^_': 4, 'FRS}W': 4, 'FB^TW': 4, 'FIN\\o': 3, 'FYS{w': 3, 'FQ\\sw': 4, 'FRT\\W': 4, 'FB]^G': 3, 'FHN]o': 3, 'FBZ\\o': 4, 'FJY[w': 3, 'FqSxw': 3, 'FYaZw': 4, 'FqIZw': 4, 'Fk_zw': 3, 'FK`~o': 3, 'FwEZw': 3, 'FBrlo': 4, 'FRqiw': 4, 'FQNmo': 4, 'FRpkw': 3, 'FRrHw': 3, 'F`Nmo': 3, 'F@z^_': 3, 'FBfnO': 3, 'FFqjW': 3, 'FJqkw': 4, 'F?~v_': 2, 'FqG^w': 4, 'FwC^w': 2, 'F@\\zw': 2, 'FILzw': 2, 'F@lzw': 3, 'F@L~w': 3, 'F?\\~w': 3, 'FAL~w': 4, 'F@tzw': 4, 'FC\\zw': 3, 'F@\\vw': 3, 'F@^rw': 3, 'FBYzw': 3, 'FPTzw': 4, 'F`Lzw': 3, 'FJYZw': 3, 'FJX\\w': 3, 'F?N~w': 4, 'F?l~w': 4, 'FCL~w': 4, 'F@N^w': 3, 'F@uzw': 4, 'FAmzw': 4, 'F@lvw': 4, 'F`K~w': 2, 'FDYzw': 4, 'F@]~g': 3, 'FDhzw': 3, 'F`Mzw': 3, 'F@N~o': 3, 'FGF~w': 3, 'FGU~w': 4, 'FGd~w': 3, 'F_L~w': 4, 'F?^vw': 3, 'F@^mw': 4, 'FC\\~W': 3, 'F?^~o': 3, 'FBUnw': 4, 'FQS~w': 4, 'FIM^w': 4, 'FBY^w': 3, 'FQL}w': 4, 'FBp|w': 4, 'FAl~g': 4, 'F@^^g': 4, 'FId|w': 4, 'FQdzw': 4, 'FIN\\w': 3, 'FBd~W': 3, 'FQT|w': 4, 'FAN~o': 4, 'FBZ\\w': 3, 'FEhzw': 4, 'FHN]w': 3, 'FKdzw': 3, 'FD^bw': 3, 'FLLmw': 4, 'FXL]w': 3, 'FP\\uw': 3, 'FpLZw': 3, 'FQ\\tw': 4, 'FB^dw': 3, 'FTXZw': 4, 'FS\\rw': 3, 'F`\\tw': 3, 'FhK}w': 3, 'FB^vO': 3, 'FJ^cw': 3, 'FK`~w': 3, 'FBqnw': 4, 'F@zVw': 3, 'F`h^w': 4, 'F`o~w': 3, 'FaM~W': 4, 'FQNmw': 4, 'F_^tw': 3, 'FENnW': 3, 'F`Nmw': 3, 'F_N~o': 3, 'F?~vg': 2, 'FLU^W': 4, 'FRqZw': 3, 'FQurw': 4, 'FFdnW': 3, 'FBuvW': 4, 'FPvRw': 3, 'FFqjw': 3, 'FqMZw': 3, 'FMiZw': 4, 'FYeZw': 3, 'FJe^W': 3, 'FD^vO': 3, 'FRluW': 4, 'FJmuW': 3, 'F`l~_': 3, 'FdlrW': 3, 'FbmrW': 3, 'F@~v_': 3, 'FB\\zw': 2, 'F@\\~w': 3, 'FD\\zw': 3, 'FIL~w': 3, 'FI\\|w': 3, 'FK\\zw': 3, 'F@N~w': 3, 'F@l~w': 3, 'FDlzw': 3, 'F?^~w': 3, 'FAN~w': 4, 'F@t~w': 4, 'FC\\~w': 3, 'FB^\\w': 3, 'FPT~w': 4, 'FHN^w': 3, 'FBY~w': 3, 'F`L~w': 3, 'FBnjw': 3, 'FD\\~W': 3, 'FQlzw': 4, 'F@^~o': 3, 'F`lzw': 3, 'FImzw': 3, 'FS\\zw': 3, 'FJY^w': 3, 'FJp|w': 3, 'FIl~g': 3, 'FB^vW': 3, 'FMhzw': 3, 'FIN~o': 3, 'F_N~w': 3, 'F@z^w': 3, 'F?~vw': 2, 'FQd~w': 4, 'FEh~w': 4, 'FENnw': 3, 'FKd~w': 3, 'F`uzw': 4, 'FBz\\w': 3, 'FHv\\w': 3, 'F@v~o': 3, 'FD^fw': 3, 'FTX^w': 4, 'F`lvw': 3, 'FLh^w': 3, 'FDx~g': 3, 'FLY}w': 4, 'FD^vW': 3, 'FRqzw': 3, 'FLh}w': 3, 'F`]~g': 3, 'FdYzw': 3, 'FDZ~o': 4, 'Fdhzw': 3, 'FJq|w': 3, 'F@~vg': 3, 'F`N~o': 2, 'FjY\\w': 3, 'FjNLw': 3, 'FJzTw': 3, 'FMnbw': 3, 'FFzbw': 3, 'FrzPw': 3, 'F^rHw': 2, 'FJ\\zw': 1, 'FB\\~w': 3, 'FR\\zw': 3, 'F@^~w': 3, 'FD\\~w': 3, 'FT\\zw': 3, 'FIN~w': 3, 'FI]~w': 3, 'FK\\~w': 3, 'FJ^\\w': 3, 'FR\\}w': 3, 'FB^~o': 3, 'F?~~w': 2, 'FC^~w': 3, 'FEl~w': 3, 'FDZ~w': 4, 'F`N~w': 2, 'FBnnw': 3, 'FQl~w': 4, 'FIm~w': 3, 'F`l~w': 3, 'F@~vw': 3, 'FMmzw': 3, 'FD^~o': 3, 'Fdlzw': 3, 'FbY~w': 3, 'FJq~w': 3, 'FMh~w': 3, 'FL^mw': 3, 'F[\\}w': 3, 'FBz~o': 3, 'FF^nW': 3, 'FK^~o': 3, 'FJz\\w': 3, 'Fs\\zw': 2, 'Fro~w': 3, 'F]o~w': 2, 'Fd^vW': 3, 'FFzvW': 3, 'F`~vg': 2, 'FqN~o': 3, 'FJ\\~w': 2, 'FB^~w': 3, 'FR\\~w': 3, 'FJ^~o': 2, 'F@~~w': 3, 'FD^~w': 3, 'FT\\~w': 3, 'FIn~w': 3, 'FK^~w': 3, 'FJu~w': 3, 'FR^^w': 3, 'FB~vw': 3, 'FR^~o': 3, 'Ft\\zw': 2, 'FqN~w': 3, 'FRz^w': 3, 'FFznw': 2, 'F`~vw': 2, 'FMn~o': 3, 'F]uzw': 3, 'FF~vW': 2, 'FJ^~w': 2, 'FB~~w': 3, 'FR^~w': 3, 'FJ~vw': 2, 'F`~~w': 2, 'FMn~w': 3, 'FFz~w': 2, 'FR~vw': 3, 'Ft\\~w': 2, 'FN~vW': 2, 'FJ~~w': 2, 'FF~~w': 2, 'FR~~w': 3, 'FNz~w': 2, 'F}l~w': 2, 'FN~~w': 2, 'Fr~~w': 2, 'F^~~w': 2, 'F~~~w': 1, 'G???F{': 2, 'G??CB{': 3, 'G???N{': 3, 'G?A?Js': 4, 'G??E@{': 4, 'G??GVk': 4, 'G??CJ{': 4, 'G???^{': 4, 'G??EHw': 4, 'G??F?{': 4, 'G??CZw': 4, 'G??EH{': 4, 'G???~w': 4, 'G??CZ{': 4, 'G???~{': 4, 'G??EXw': 4, 'G??Czw': 4, 'G??EX{': 4, 'G??@~w': 4, 'G??Cz{': 4, 'G??@~{': 4, 'G??Dzw': 4, 'G??B~w': 3, 'G??Dz{': 4, 'G??B~{': 3, 'G??F~w': 2, 'G??F~{': 2, 'G?AA@{': 4, 'G??KB{': 4, 'G?C?N{': 4, 'G?AAHs': 5, 'G?_GJc': 5, 'G??KRk': 5, 'G?_?Zk': 5, 'G?COVK': 5, 'G?AAH{': 5, 'G?C?n[': 5, 'G?A?Z{': 5, 'G??O^{': 5, 'G?_I@k': 5, 'G?AB?{': 5, 'G?CSB[': 5, 'GC?Gb[': 5, 'G?_AH{': 5, 'G??M@{': 5, 'G?C`E{': 5, 'GC??Z{': 5, 'G?CCJ{': 5, 'G@??^{': 5, 'G??G^c': 3, 'G??G^k': 3, 'G??G^{': 3, 'G??MPg': 5, 'G?AIHs': 5, 'GC??zW': 5, 'G?B?Xs': 5, 'G?CCjW': 5, 'G??MHk': 5, 'G??MPk': 5, 'G??[Js': 5, 'G?AOZs': 5, 'G@?@]w': 5, 'G?AAX{': 5, 'GC??z[': 5, 'G??MH{': 5, 'G?CCj[': 5, 'G??o^s': 5, 'G?A?z{': 5, 'G??SZ{': 5, 'G@?@]{': 5, 'G??_~{': 5, 'G?@CXo': 5, 'GC?AXw': 5, 'G?CEHw': 5, 'G?@CXs': 5, 'G??KZc': 4, 'GO??zw': 5, 'G@?CZw': 5, 'GC?AX{': 5, 'G?CEH{': 5, 'GG??~w': 4, 'GO??z{': 5, 'G@?CZ{': 5, 'GG??~{': 4, 'G?AGZc': 4, 'G?C?~G': 4, 'G??WnS': 4, 'G?_GZk': 4, 'G??KZk': 4, 'G?C?~K': 4, 'G?CG^k': 4, 'G??O~[': 4, 'G??KZ{': 4, 'G??G~{': 4, 'G??cyw': 5, 'G??Mhw': 5, 'G??Lrg': 5, 'G?A@zw': 4, 'G??czw': 5, 'GG?A|w': 4, 'G??cy{': 5, 'G??Mh{': 5, 'G??Lrk': 5, 'G?@@~w': 4, 'G?A@z{': 4, 'G??cz{': 5, 'GG?A|{': 4, 'G?@@~{': 4, 'G?A@zo': 5, 'G@?@}W': 5, 'G_?@zw': 4, 'GG?Czw': 4, 'G?A@zs': 5, 'G@?@}[': 5, 'G_?@~w': 3, 'G_?@z{': 4, 'GG?Cz{': 4, 'G_?@~{': 3, 'G??MXw': 5, 'G??`}w': 5, 'G??Kzw': 5, 'G??MX{': 5, 'G??H~w': 5, 'G??`}{': 5, 'G??Kz{': 5, 'G??H~{': 5, 'G?ABzw': 3, 'G??Njw': 4, 'G??Nvg': 3, 'G?AB~w': 3, 'G?ABz{': 3, 'G??Nj{': 4, 'G??Nvk': 3, 'G?AB~{': 3, 'G??Lzw': 5, 'G??J~w': 4, 'G??Lz{': 5, 'G??J~{': 4, 'G??N~w': 3, 'G??N~{': 3, 'G?CO^C': 4, 'G??WvK': 4, 'G?CO^K': 4, 'G??Wv[': 4, 'G?CO^{': 4, 'GCCGJC': 6, 'GC?GrK': 6, 'G?K_eK': 6, 'G?Q?Xk': 6, 'GCC?ZK': 6, 'G?CKbK': 6, 'G?AIPk': 6, 'G?GPe[': 6, 'GC?OZ[': 6, 'G?CSJ[': 6, 'G@G?m[': 6, 'G?AIP{': 6, 'G?AOr[': 6, 'G?GPM{': 6, 'G?_Gj{': 6, 'G??pU{': 6, 'G??gv{': 6, 'GCOOPK': 6, 'G?@KPc': 6, 'G??MHg': 5, 'GCG_a[': 6, 'GCCAH[': 6, 'G?CU@[': 5, 'G?B@O{': 5, 'GAO`C{': 5, 'GP??Y{': 6, 'G@GCI{': 5, 'G??]@{': 5, 'G?AQP{': 5, 'GI??\\{': 5, 'G??sR{': 5, 'G?@_v{': 5, 'G??[rG': 5, 'G?_WrK': 5, 'G@?gmS': 5, 'G?cGjK': 5, 'G??xeS': 5, 'G?ChUk': 5, 'GC?Wr[': 5, 'G?KHMk': 5, 'G?CSZ[': 5, 'G@?_}[': 5, 'G?CKj[': 5, 'G??pu[': 5, 'G@?Wv[': 5, 'G?G_}{': 5, 'G?CSZ{': 5, 'G?GHm{': 5, 'G?CP^{': 5, 'G??\\bO': 6, 'G??[jO': 5, 'G?AQXo': 6, 'G?IPIs': 6, 'GO?XIs': 5, 'GI?@[w': 5, 'G?oGhk': 5, 'G?cIHk': 6, 'G?ApQs': 6, 'G??|As': 5, 'G?CKjK': 5, 'G?GKik': 6, 'G??\\bS': 6, 'G?OqLs': 5, 'G?gGjk': 6, 'G?KKJk': 5, 'G?@qTs': 5, 'G@?cY{': 6, 'GO?_y{': 5, 'GI?@[{': 5, 'G?CMH{': 5, 'G?_Ih{': 6, 'G??tQ{': 6, 'G?A`q{': 5, 'G?WGnk': 5, 'GG@?|{': 5, 'G?GKj{': 6, 'G?_Hj{': 5, 'G?@at{': 5, 'G?OHn{': 5, 'G?K@mG': 5, 'G?A`qo': 6, 'GI?CXw': 5, 'Gg??xw': 5, 'G?B_ps': 5, 'G?AqPs': 5, 'G??}@s': 4, 'G?K@mK': 5, 'G?A`qs': 6, 'G??^?{': 4, 'G??m_{': 5, 'Go??zw': 4, 'G?B_rs': 5, 'G?@sRs': 4, 'GI?CX{': 5, 'Gg??x{': 5, 'G??uP{': 5, 'G?Aap{': 5, 'G?B@p{': 4, 'G?B_vs': 4, 'Go??z{': 4, 'G?@cr{': 5, 'G?B@r{': 4, 'G?B@v{': 4, 'G?CW^C': 4, 'G?CWvK': 4, 'G?CG~K': 4, 'G??W~K': 4, 'G?CO~[': 4, 'G??W~[': 4, 'G??W~{': 4, 'G?_WZc': 5, 'G??p]o': 5, 'G?@KXs': 5, 'G??]`[': 5, 'G??sY[': 5, 'G?GW^c': 5, 'G?_Gzk': 5, 'G?CKZk': 5, 'G??p]s': 5, 'G?AIX{': 5, 'G?AOz[': 5, 'G?GG~k': 5, 'G?AGz{': 5, 'G??p]{': 5, 'G??g~{': 5, 'G??sZo': 5, 'G?@co{': 5, 'G??kqk': 6, 'G??[rK': 5, 'G?@_~o': 5, 'G?A_zs': 5, 'G??sZs': 5, 'G??]H{': 5, 'G?AQX{': 6, 'G?@_~s': 5, 'G??sZ{': 5, 'G?@_~{': 5, 'G?CTZW': 5, 'G?P@|w': 5, 'G?CTZw': 5, 'G?OJlw': 5, 'G?CTZ[': 5, 'G?CR^w': 5, 'G?P@|{': 5, 'G?CTZ{': 5, 'G?OJl{': 5, 'G?CR^{': 5, 'G?CNJg': 5, 'G?_Jjg': 4, 'G??^fO': 4, 'G?GH}g': 5, 'G_A@zw': 4, 'G?OLjw': 5, 'G?_Jjw': 4, 'G?BDrw': 4, 'G?CNJk': 5, 'G?_Jjk': 4, 'G??^fS': 4, 'G?GH}k': 5, 'G?_Jnw': 4, 'G_A@z{': 4, 'G?OLj{': 5, 'G?_Jj{': 4, 'G?BDr{': 4, 'G?_Jn{': 4, 'G?CSzW': 5, 'G?CP~W': 5, 'G?AWzs': 5, 'G??x]s': 5, 'G?CSz[': 5, 'G??w~s': 5, 'G?CP~[': 5, 'G??[z{': 5, 'G??h}{': 5, 'G??X~{': 5, 'G??\\Zo': 5, 'G?AHzo': 5, 'G??^bW': 5, 'G?OH~g': 5, 'G?Agzs': 5, 'G??{Zs': 5, 'G?@q\\s': 5, 'G??\\Zs': 5, 'G?AHzs': 5, 'G??^b[': 5, 'G??]X{': 5, 'G??ky{': 5, 'G??\\j[': 5, 'G?@g~s': 5, 'G?OH~k': 5, 'G??kz{': 5, 'G?AHz{': 5, 'G?@a|{': 5, 'G?@H~{': 5, 'G??ZvG': 5, 'G?AJrg': 4, 'G?B@~o': 4, 'G?B_zs': 5, 'G?@sZs': 4, 'G??ZvK': 5, 'G?AJrk': 4, 'G??X~K': 5, 'G?@Lh{': 5, 'G?B@x{': 4, 'G?B_~s': 4, 'G?B@~s': 4, 'G?@cz{': 5, 'G?B@z{': 4, 'G?B@~{': 4, 'G?CV^W': 4, 'G?CV^w': 4, 'G?CV^[': 4, 'G?CV^{': 4, 'G?CR~W': 5, 'G??\\zw': 5, 'G??Z~w': 5, 'G?CR~[': 5, 'G??\\z{': 5, 'G??Z~{': 5, 'G??^^o': 4, 'G??^Zw': 5, 'G?AJzw': 4, 'G??^nW': 4, 'G?AJ~w': 4, 'G??^^s': 4, 'G??^Z{': 5, 'G?AJz{': 4, 'G??^n[': 4, 'G?AJ~{': 4, 'G??^~w': 4, 'G??^~{': 4, 'G@GWuK': 4, 'G??xuK': 4, 'G?Kpe[': 4, 'G@CP][': 4, 'G??xu[': 4, 'G@G_}{': 4, 'G??xu{': 4, 'G??xv{': 4, 'GCGWrK': 5, 'G?XO\\c': 5, 'G??{qs': 5, 'G??|Qs': 5, 'G??kyw': 5, 'G??|Is': 5, 'GAGWvK': 5, 'GCCPZ[': 5, 'G@CSZ[': 5, 'G?WIlk': 5, 'G?AYp{': 5, 'G?Ahq{': 5, 'G?@rS{': 5, 'GACP^[': 5, 'G?AXr{': 5, 'G?@it{': 5, 'G?@Xv{': 5, 'G?@rSo': 5, 'G?YOZc': 5, 'G?Bcro': 4, 'G?BHps': 4, 'G?Ahqs': 6, 'G?AZbS': 5, 'G?KHmK': 4, 'G??zeS': 5, 'G?BGxs': 5, 'G??xmS': 5, 'G??\\jW': 6, 'G?oo^c': 4, 'G?oHjk': 5, 'G?WKjk': 5, 'G?Bcrs': 4, 'G??}P{': 4, 'G?Aip{': 6, 'G?@uP{': 5, 'G?oHnk': 4, 'G?@kr{': 5, 'G?Bcr{': 4, 'G?BHv{': 4, 'G??|ro': 4, 'G@Ga}w': 4, 'G?Axrs': 4, 'G?@yts': 5, 'G??|rs': 4, 'G?@xvs': 4, 'G@Ga}{': 4, 'G??|r{': 4, 'G?@Zt{': 5, 'G??zv{': 4, 'GACR\\W': 5, 'G?AZro': 4, 'G??~Uo': 4, 'G?BXps': 4, 'G?AXzo': 5, 'G?@i|o': 5, 'G?@zSs': 5, 'G?Bczo': 4, 'GCCR^W': 4, 'G?BXrs': 5, 'G?@{rs': 4, 'G?Bkrs': 4, 'GACR\\[': 5, 'G?AZrs': 4, 'G??~Us': 4, 'G??}p{': 4, 'G?BXvs': 4, 'GCCR^[': 4, 'G?@\\r{': 5, 'G?AZr{': 4, 'G?BLr{': 4, 'G?AZv{': 4, 'G??x~o': 4, 'G??x~s': 4, 'G??x}{': 4, 'G??x~{': 4, 'G?@X~o': 5, 'G?@\\p{': 5, 'G??|q{': 5, 'G??~Q{': 5, 'G?AYx{': 5, 'G?@X~s': 5, 'G?AXz{': 5, 'G?@i|{': 5, 'G?@X~{': 5, 'G?BH~o': 4, 'G?AZr[': 5, 'G??zu[': 5, 'G??~e[': 4, 'G??x}[': 4, 'G??|Y{': 5, 'G?@r[{': 5, 'G?BH~s': 4, 'G?@kz{': 5, 'G?Bcz{': 4, 'G?BH~{': 4, 'G??~vo': 4, 'G??~vw': 4, 'G??~vs': 4, 'G??~v{': 4, 'G??~rw': 4, 'G?@x~s': 4, 'G??~r{': 4, 'G??|z{': 4, 'G??z~{': 4, 'G??~uw': 4, 'G?BX~s': 4, 'G??~u{': 4, 'G??}z{': 5, 'G?AZz{': 4, 'G??~]{': 4, 'G?AZ~{': 4, 'G??~~w': 4, 'G??~~{': 4, 'G?Azro': 4, 'G?@zvo': 3, 'G?@zs{': 4, 'G?@zvs': 3, 'G?@zt{': 4, 'G?@zv{': 3, 'G?B\\ro': 4, 'G?Azvo': 4, 'G?Azrs': 4, 'G?@|rs': 4, 'G?@}ts': 4, 'G??|zw': 4, 'G?@y|s': 5, 'G??~]w': 4, 'G?Azvs': 4, 'G?Azr{': 4, 'G?B\\r{': 4, 'G?Azv{': 4, 'G?@~vo': 3, 'G?@z~o': 3, 'G?Az~o': 4, 'G?Bzvs': 3, 'G?@~vs': 3, 'G?@~v{': 3, 'G?@~r{': 3, 'G?Azz{': 4, 'G?@z~{': 3, 'G?@~t{': 4, 'G?B\\z{': 4, 'G?Az~{': 4, 'G?@~~{': 3, 'G?B~vo': 2, 'G?B~vs': 2, 'G?@~~w': 3, 'G?B~v{': 2, 'G?B~~{': 2, 'G?`@?{': 5, 'G?EA@{': 5, 'G@?KB{': 5, 'GGC?N{': 4, 'G?GSQK': 6, 'G?cQ@K': 6, 'G?EA`[': 6, 'GA_?h[': 6, 'G@GSA[': 6, 'GC?I`[': 5, 'GD?HA[': 6, 'G?IAG{': 6, 'G@_@I{': 6, 'G?CdA{': 5, 'GOC@I{': 5, 'GGD@C{': 5, 'G?_QH{': 6, 'G?EAH{': 5, 'G@OAL{': 5, 'G?__j{': 6, 'G?CcJ{': 5, 'G?D@N{': 5, 'G@EA?[': 6, 'G?`?Xc': 6, 'G@IA?{': 6, 'GOCa?{': 6, 'GCO@G{': 6, 'G?EB?{': 5, 'G@PC@{': 5, 'G`?I@{': 5, 'GQ??X{': 6, 'G@_AH{': 5, 'G@?M@{': 4, 'GGECB{': 4, 'GK??Z{': 5, 'GGCCJ{': 4, 'G`??^{': 4, 'G?E?rK': 4, 'G?_Oj[': 4, 'G@?He[': 4, 'G?C`M{': 4, 'GC?GZ{': 4, 'G@?G^{': 4, 'G?IIOk': 6, 'G@?LQg': 6, 'G?EIPk': 5, 'G?QGpk': 6, 'GO?oYs': 6, 'G?GsIs': 5, 'G@A_Ys': 6, 'GAGBKw': 5, 'G?GSY[': 6, 'GA?Kh[': 5, 'G?Cci[': 6, 'G?GTa[': 6, 'G?CkRk': 5, 'G?_grk': 5, 'GA@_\\s': 5, 'G?`?x{': 5, 'G?_QX{': 6, 'GO?PY{': 6, 'G@A@Y{': 5, 'G@?LI{': 6, 'GAGBK{': 5, 'G?DHVk': 5, 'G?I?z{': 5, 'G?GSZ{': 5, 'GG?Q\\{': 5, 'G?O_~{': 5, 'G?`@pg': 6, 'G?I@io': 6, 'G@A@qW': 5, 'G@?HuG': 5, 'G?_qHs': 5, 'GAA_Xs': 6, 'GK?AXw': 5, 'G?EaHs': 5, 'G`?AXw': 5, 'G@B?Xs': 4, 'G@OEHw': 5, 'G?__yk': 6, 'G?`@pk': 6, 'G@?MG{': 5, 'G?I@is': 6, 'G?C_}K': 5, 'G@A@q[': 5, 'G@?HuK': 5, 'GC@_Zs': 5, 'G?DcJs': 4, 'G@B?Zs': 5, 'GK?CZw': 4, 'GO@?x{': 5, 'GO?QX{': 6, 'GK?AX{': 5, 'G@AAX{': 5, 'G`?AX{': 5, 'G@?MH{': 4, 'G@OEH{': 5, 'G@B?^s': 4, 'G_?_z{': 5, 'GGA?z{': 4, 'GG?SZ{': 5, 'GK?CZ{': 4, 'G_?_~{': 4, 'G?EGrK': 5, 'GCCGZK': 5, 'G?GomS': 5, 'G@?o]S': 5, 'G?C[b[': 5, 'G?Gguk': 5, 'G@GG]k': 5, 'G?_Oz[': 5, 'GC?Gz[': 5, 'G?C`m[': 5, 'G@?Hm[': 5, 'G?CXf[': 5, 'G?E?z{': 5, 'G?GP]{': 5, 'G@?H]{': 5, 'G?C_~{': 5, 'G?_pIs': 5, 'GA_GXk': 5, 'G?E`Is': 5, 'GGCBKw': 5, 'G@?La[': 5, 'GCGGZk': 5, 'G@@ILs': 5, 'G@_GZk': 5, 'GC?`Y{': 5, 'GC?IX{': 5, 'G?CdI{': 5, 'GGCBK{': 4, 'G@OG^k': 4, 'GO?Gz{': 5, 'G@@A\\{': 5, 'G@?KZ{': 4, 'GG?G~{': 4, 'G?`@xw': 4, 'G?I@yw': 5, 'G_?Jhw': 5, 'G?EBjW': 4, 'G?GP}W': 4, 'GA?NHw': 5, 'G@?NUg': 4, 'G?Q@zw': 4, 'G?Oczw': 5, 'G_?czw': 4, 'G?`@x{': 4, 'G?I@y{': 5, 'G_?Jh{': 5, 'G?EBj[': 4, 'G?GP}[': 4, 'GA?NH{': 5, 'G@?NUk': 4, 'G?`@~w': 4, 'G?Q@z{': 4, 'G?Ocz{': 5, 'G_?cz{': 4, 'G?`@~{': 4, 'G?Ccyw': 5, 'G?GTYw': 6, 'G@?LYw': 5, 'G?E@zw': 5, 'G?HA|w': 5, 'G?Cczw': 5, 'GG?I|w': 5, 'G?Ccy{': 5, 'G?GTY{': 6, 'G@?LY{': 5, 'G?D@~w': 5, 'G?E@z{': 5, 'G?HA|{': 5, 'G?Ccz{': 5, 'GG?I|{': 5, 'G?D@~{': 5, 'GC?HzW': 5, 'GG?Jkw': 5, 'G@?NeW': 4, 'G@?H}W': 4, 'G_?Hzw': 5, 'GGACzw': 4, 'GG?Kzw': 4, 'GC?Hz[': 5, 'GG?Jk{': 5, 'G@?Ne[': 4, 'G@?H}[': 4, 'G_?H~w': 4, 'G_?Hz{': 5, 'GGACz{': 4, 'GG?Kz{': 4, 'G_?H~{': 4, 'G?C`}w': 4, 'G@?H~w': 4, 'G?C`}{': 4, 'G@?H~{': 4, 'G?EBzw': 4, 'G?GV]w': 4, 'G?DB|w': 5, 'G@?N]w': 4, 'G?EB~w': 4, 'G?EBz{': 4, 'G?GV]{': 4, 'G?DB|{': 5, 'G@?N]{': 4, 'G?EB~{': 4, 'G@?Lzw': 4, 'G@?J~w': 4, 'G@?Lz{': 4, 'G@?J~{': 4, 'G@?N~w': 4, 'G@?N~{': 4, 'G?G[Ic': 6, 'G?G\\Ac': 6, 'GAL@CK': 6, 'G?CciW': 6, 'G?E`a[': 6, 'GO?oq[': 6, 'GHO?k[': 6, 'GAH@c[': 6, 'GA_Gh[': 6, 'G@CcI[': 6, 'GOC_i[': 6, 'GD?_Y[': 6, 'G?_Y`[': 6, 'G@A_q[': 6, 'G?HRC{': 6, 'G@GKI{': 6, 'GOGGi{': 6, 'GGOPK{': 6, 'GAH@K{': 6, 'G?g_i{': 6, 'G?IHa{': 6, 'GG@PS{': 6, 'G?EQP{': 6, 'GAGIL{': 6, 'G?DaT{': 6, 'GCCHJ{': 6, 'G?DPV{': 6, 'G?E`aS': 6, 'G?M@aK': 5, 'GDP@?[': 6, 'GKO__[': 6, 'G?KSIK': 6, 'G?CKjG': 5, 'G?GSiW': 5, 'G@APQS': 6, 'G?_WjC': 5, 'G?GXeC': 5, 'G?AIXo': 5, 'GAOd?{': 5, 'GaG@G{': 6, 'GQO@G{': 5, 'GIIC?{': 5, 'GOGQG{': 6, 'G@IAG{': 5, 'G?IR?{': 5, 'GO?Z?{': 5, 'GY??W{': 6, 'G?Gu?{': 5, 'GO?qO{': 5, 'GIGCG{': 5, 'G?o_g{': 5, 'G?`H_{': 5, 'GSOAH{': 5, 'GAOcH{': 5, 'G_O_h{': 6, 'G?Ou@{': 5, 'GA@cP{': 5, 'G_?qP{': 5, 'Gq??X{': 5, 'G?II`{': 5, 'G?MAH{': 5, 'G?G]@{': 5, 'GC`@J{': 5, 'G?`cb{': 5, 'G?WSJ{': 5, 'G?Okb{': 5, 'G?`Hf{': 5, 'G?CpUK': 5, 'G?K_mK': 5, 'G?GXe[': 5, 'G@?gu[': 5, 'G?CpU{': 5, 'G@GO^{': 5, 'G?ClQk': 5, 'G?WYLc': 5, 'G?Ckqk': 5, 'G?GsYs': 5, 'GCKOZK': 5, 'G?HItk': 5, 'G@CKj[': 5, 'GCCHj[': 5, 'G?X?|k': 5, 'GAKO^K': 5, 'G?I_y{': 5, 'G?IHi{': 5, 'GG@P[{': 5, 'G?EQX{': 5, 'GACHn[': 5, 'G?P_|{': 5, 'G?EPZ{': 5, 'G?DP^{': 5, 'G?G[rG': 6, 'G?G^E_': 5, 'G?G[Z_': 6, 'GG@P[o': 6, 'G?LM@k': 5, 'G?daPk': 6, 'G_AqPs': 5, 'G__qHs': 5, 'GDCIH[': 6, 'G?\\CHk': 5, 'G_KIHk': 5, 'GECHH[': 5, 'G?saHk': 6, 'GAgIHk': 6, 'G?Qu@s': 5, 'G?I_ys': 6, 'GCCJJK': 5, 'G?KP]K': 5, 'GA?^@[': 6, 'G@CMJK': 6, 'G?G^Ec': 5, 'G?EOzS': 5, 'GCCHZK': 6, 'G?GX]c': 5, 'G@CH]K': 5, 'G?G]bK': 6, 'G?NCRk': 5, 'GBCKJ[': 5, 'GECHJ[': 6, 'G?lCJk': 5, 'GCWKJk': 5, 'G?p@h{': 5, 'G?XCh{': 6, 'G_Aap{': 5, 'Go@?x{': 5, 'GCCJH{': 6, 'G?QJ`{': 5, 'G_OHh{': 5, 'G@CMH{': 5, 'G?HM`{': 6, 'GGOKh{': 6, 'GOBAp{': 5, 'GECHN[': 5, 'G?q@j{': 5, 'GCCJJ{': 5, 'GACLJ{': 6, 'G?QLb{': 5, 'G__Hj{': 5, 'GCCJN{': 5, 'G?KXeK': 5, 'G@KO]K': 5, 'G?KPm[': 5, 'G@CHm[': 5, 'G@C_}[': 5, 'G@GXe[': 5, 'G?Cp][': 5, 'G@?g}[': 5, 'G@C`]{': 5, 'G?GXm{': 5, 'G?Cp]{': 5, 'G?Cp^{': 5, 'G?LJCk': 5, 'GCCha[': 5, 'GGSHKk': 5, 'GGDHSk': 5, 'GDCHI[': 5, 'G?\\@Kk': 5, 'G@GSY[': 5, 'G@DId[': 5, 'GBCIL[': 5, 'GOCpQ{': 5, 'G?X@k{': 5, 'G@CcY{': 5, 'GGOHk{': 5, 'GGO_{{': 5, 'G@CLI{': 5, 'G?Ojc{': 5, 'GGCpU{': 5, 'GAD@\\{': 5, 'GACJL{': 5, 'G@GSZ{': 5, 'G@GQ^{': 5, 'G@CW^C': 5, 'G?CXvK': 5, 'G?EOz[': 5, 'G?Gg}k': 5, 'G@CG~K': 5, 'G?_Wz[': 5, 'GC?Wz[': 5, 'G?Ch]k': 5, 'G?Co~[': 5, 'G?_Wz{': 5, 'G?Gg}{': 5, 'G@?W~[': 5, 'G?GW~{': 5, 'G?G[Zc': 5, 'G?EHZc': 6, 'G?Og~_': 5, 'G?CsY[': 5, 'G?`HW{': 5, 'G?Og~c': 5, 'G?CkZk': 5, 'G?_gzk': 5, 'G?`Gx{': 5, 'G?DH^k': 5, 'G?G[Z{': 5, 'G?Og~{': 5, 'G?aRZo': 5, 'G?EJrg': 5, 'G?DRtW': 5, 'G?G]vG': 5, 'G?`kjs': 5, 'G?DsZs': 5, 'G?FPZs': 5, 'G?b_zs': 5, 'GCCJnW': 5, 'G?ERZ[': 5, 'G?Cr][': 5, 'G?G]nK': 5, 'G?aRZs': 5, 'G?DLh{': 5, 'G?EJrk': 5, 'G?Cmh{': 5, 'G?O^H{': 5, 'G?DRt[': 5, 'G?G]vK': 5, 'G?FP^s': 5, 'G?b@z{': 5, 'G?ERZ{': 5, 'G?DTZ{': 5, 'G?`Lj{': 5, 'GCCJn[': 5, 'G?ER^{': 5, 'G?G\\rg': 5, 'GA?y\\s': 5, 'G?Dq\\s': 5, 'G?Iozs': 5, 'G?Po|s': 5, 'G@Cb]w': 5, 'G@?ky{': 5, 'G?G\\rk': 5, 'G?Ho~s': 5, 'GA@H|{': 5, 'G?DR\\{': 5, 'G@?kz{': 5, 'GA?Z\\{': 5, 'G@Cb]{': 5, 'G@?i~{': 5, 'G@?m]o': 5, 'G?G^Ug': 5, 'GA?ZtW': 5, 'GC@kZs': 5, 'G?FcZs': 5, 'G?JOzs': 5, 'G?`ozs': 5, 'G?cRnW': 5, 'G@?]Z[': 5, 'GC?ZZ[': 5, 'G@?m]s': 5, 'G?OZ\\k': 5, 'G?G^Uk': 5, 'G?G]h{': 5, 'G?_Xzk': 5, 'GA?Zt[': 5, 'G?JO~s': 5, 'G_AHz{': 5, 'G?QLj{': 5, 'GA?\\Z{': 5, 'GC?ZZ{': 5, 'G?cRn[': 5, 'GC?Z^{': 5, 'GAD@|W': 5, 'G@GU]W': 5, 'G@GP}W': 5, 'GCEBZw': 5, 'GCCNJw': 5, 'G@GUZw': 5, 'GAD@|[': 5, 'G@GU][': 5, 'G@GP}[': 5, 'G@GU^w': 5, 'GCEBZ{': 5, 'GCCNJ{': 5, 'G@GUZ{': 5, 'G@GU^{': 5, 'G@CI~G': 5, 'G?DXnS': 5, 'G?MGzk': 5, 'G?cgzk': 5, 'G?Si\\k': 5, 'G@@W~S': 5, 'G?Cli{': 5, 'G@CI~K': 5, 'G?G[y{': 5, 'G?G\\Y{': 5, 'G?G[zk': 5, 'G?LG~k': 5, 'G?DP~[': 5, 'G?_Xz{': 5, 'G?G[z{': 5, 'G?HI|{': 5, 'GA?X~[': 5, 'G?OX~{': 5, 'G?G]^_': 5, 'G?JG~c': 5, 'G?LKZk': 5, 'G?dHZk': 5, 'G?EJj[': 5, 'G?G]Zk': 5, 'G?_ZZk': 5, 'G?G]^c': 5, 'G?IHy{': 5, 'G?`Hx{': 5, 'G?GX}[': 5, 'G?MI^k': 5, 'G?`H~k': 5, 'G?QHz{': 5, 'G?Okz{': 5, 'G?`H~{': 5, 'G@?x]s': 5, 'G?Kg}k': 5, 'G?Kg~k': 5, 'G@?h}{': 5, 'G?GX}{': 5, 'G?GX~{': 5, 'G@?m}w': 5, 'G@?Z~W': 5, 'G?G^vg': 5, 'G@?m~w': 5, 'G@?m}{': 5, 'G@?Z~[': 5, 'G?G^vk': 5, 'G@?m~{': 5, 'G?Cnmw': 5, 'G?_Zzw': 5, 'G?OZ|w': 5, 'G?G^]w': 5, 'G?G]~g': 5, 'G?_Z~w': 5, 'G?Cnm{': 5, 'G?_Zz{': 5, 'G?OZ|{': 5, 'G?G^]{': 5, 'G?G]~k': 5, 'G?_Z~{': 5, 'G?G\\zw': 5, 'G?GZ~w': 5, 'G?G\\z{': 5, 'G?GZ~{': 5, 'G?G^~w': 5, 'G?G^~{': 5, 'G?_pa[': 5, 'GI?Hc[': 5, 'G@__i[': 5, 'G?DbC{': 4, 'GC?hQ{': 5, 'GGD@K{': 5, 'G@@IT{': 4, 'GOCOZ{': 5, 'GGCO^{': 4, 'G?G\\A_': 7, 'G@`@Ok': 6, 'GBOc?[': 6, 'G@`?Xc': 5, 'GL?I?[': 6, 'GCOOXK': 6, 'G?`PPc': 6, 'G@E@IS': 6, 'G@AHaS': 5, 'G?GKig': 6, 'GAIB?{': 6, 'GODB?{': 5, 'GWEA?{': 5, 'GOOPG{': 6, 'G@_aG{': 6, 'GI_@G{': 6, 'GOCaG{': 5, 'GgC@G{': 5, 'GGDD?{': 5, 'G@AIO{': 6, 'G?_r?{': 6, 'G?Eb?{': 5, 'G@`E@{': 5, 'GA_aH{': 6, 'G`?IH{': 5, 'G@PCH{': 5, 'G`_AH{': 5, 'GCGIH{': 6, 'G?`a`{': 6, 'G@AIP{': 5, 'G@@M@{': 5, 'GG_SJ{': 5, 'GC@HR{': 6, 'G@OKJ{': 5, 'GGASR{': 5, 'G@AIV{': 5, 'G?KsQK': 5, 'G?PpcS': 5, 'G?cpa[': 5, 'GGHGsk': 6, 'G@HISk': 5, 'G@cPI[': 5, 'GP?Wq[': 5, 'G?X_sk': 5, 'G@WIKk': 5, 'G?TPd[': 5, 'G?KtA{': 5, 'GADHd[': 5, 'GI?Wt[': 5, 'GCG_y{': 5, 'GGOP[{': 6, 'G@P@[{': 5, 'G@E@Y{': 5, 'GOCPY{': 5, 'G?WRK{': 5, 'G@OJK{': 5, 'G?KrE{': 5, 'GAO_|{': 5, 'G@I?z{': 5, 'GACa\\{': 5, 'GGCQ\\{': 5, 'G@H?~{': 5, 'G@G[QK': 6, 'GG?]dO': 5, 'G?EQXo': 6, 'G?G{Qc': 6, 'G?GsYo': 5, 'G?`aho': 6, 'G?C\\RG': 5, 'G?HRKo': 6, 'GA@hcS': 5, 'GAHKPk': 5, 'GA_iPk': 5, 'G_CiPk': 5, 'GaA_Xs': 5, 'GCQaHs': 5, 'GAcPH[': 6, 'G@EI`[': 5, 'G?TcPk': 5, 'G_S_Xk': 6, 'GCDH`[': 5, 'G?oi`k': 5, 'GAo_Xk': 6, 'G?Sm@k': 5, 'GAWKHk': 5, 'GCBaPs': 5, 'G@E@Y[': 6, 'GCD@X[': 5, 'G?MBIk': 5, 'GCGPY[': 6, 'GH?MG{': 6, 'GGCMHk': 6, 'GW?Ig{': 6, 'G@_JIk': 5, 'GG?]dS': 5, 'G?IPYs': 5, 'GCHKRk': 5, 'GACkb[': 5, 'GCDHb[': 5, 'G@SSJ[': 5, 'G?hKbk': 5, 'GCh?Zk': 5, 'GGQ?x{': 5, 'GAHCX{': 5, 'G_H?x{': 5, 'Go?QX{': 5, 'GQAAX{': 5, 'G@EAX{': 6, 'GCD@X{': 5, 'G?YAh{': 5, 'G_GIh{': 6, 'GCCaX{': 5, 'G?WUH{': 5, 'GAGMH{': 6, 'G?oah{': 5, 'GG_Ih{': 5, 'GO@UP{': 5, 'G@EIf[': 5, 'GOQ?z{': 5, 'GAE@Z{': 5, 'GACcZ{': 5, 'GCD@Z{': 5, 'G?ocj{': 5, 'GOOKj{': 5, 'GCD@^{': 5, 'GCChQK': 5, 'GG?[v?': 5, 'G?`r?s': 5, 'GG?ZKo': 5, 'GCHIPk': 5, 'G@`IPk': 4, 'G`AIHs': 5, 'GK?Wp[': 5, 'GCWIHk': 5, 'G@oIHk': 5, 'G@BM@s': 4, 'GCG_y[': 5, 'G_CJHk': 6, 'GGCJKk': 5, 'GG?[vC': 4, 'GCGGzK': 5, 'GG?[rK': 4, 'GGEKRk': 4, 'GQ?Wr[': 5, 'GK?Wr[': 4, 'GGcKJk': 4, 'GOP?x{': 5, 'G@PCX{': 4, 'G`AAX{': 5, 'GOCQX{': 5, 'GOOIh{': 5, 'G@OMH{': 4, 'G@BEP{': 4, 'GK?Wv[': 4, 'GGa?z{': 4, 'G_CPZ{': 5, 'GGCSZ{': 4, 'GG_Kj{': 4, 'G_CP^{': 4, 'GG@osS': 5, 'G@PHSk': 6, 'GOCXa[': 5, 'GHOG[k': 5, 'G@EHa[': 6, 'G?XHck': 6, 'GGWGkk': 5, 'G@C\\A[': 5, 'GGCYd[': 5, 'GASPL[': 6, 'G@KcI{': 5, 'GACZD[': 5, 'G@Oa[{': 6, 'GOC_y{': 5, 'GH?I[{': 5, 'GCC`Y{': 6, 'G?OrS{': 6, 'GG?ZS{': 5, 'GD?HY{': 5, 'G@KaM{': 5, 'GGD?|{': 5, 'GA?it{': 6, 'GOC_z{': 5, 'G?Dat{': 5, 'GGC_~{': 5, 'G?G\\Qg': 5, 'G?KgmC': 5, 'G?C[rG': 5, 'GC`aHs': 5, 'GI_GXk': 5, 'GaGGXk': 5, 'G?oqPk': 5, 'G?XK`k': 5, 'G_B_ps': 5, 'GCCZ@[': 5, 'G@C]@[': 4, 'GB?JK[': 5, 'GD?HY[': 5, 'GSOGZk': 4, 'G?dcRk': 5, 'GCCZB[': 5, 'GAC\\B[': 4, 'GS@AX{': 5, 'GI?KX{': 4, 'Gg?Gx{': 5, 'G?LEH{': 5, 'G?hAh{': 5, 'G_?uP{': 4, 'GD?IX{': 4, 'GE?HX{': 4, 'GCCZF[': 4, 'Go?Gz{': 4, 'G?YCj{': 5, 'GB?KZ{': 4, 'GE?HZ{': 4, 'GE?H^{': 4, 'G?MOrK': 5, 'GCCXRK': 6, 'G?XGlc': 6, 'GAHG\\c': 5, 'G?G\\Qk': 6, 'G@?kYs': 5, 'G?d?xk': 6, 'G?M@Yk': 6, 'G?E`Ys': 5, 'G@AHYs': 6, 'GG?]`[': 6, 'G?SXfK': 5, 'G?cPj[': 5, 'G?KSj[': 5, 'G?OZTk': 5, 'GGOG|k': 5, 'G@E?z[': 5, 'GCC_z[': 6, 'G?WQ\\k': 6, 'GAGI\\k': 5, 'G?_Yh{': 5, 'G?_hi{': 5, 'GO?gy{': 5, 'G?E`Y{': 6, 'G@?kY{': 5, 'G?HRK{': 5, 'G?SPn[': 5, 'GAC_~[': 5, 'GC?XZ{': 5, 'G?IOz{': 5, 'G?Da\\{': 5, 'GA?i\\{': 5, 'G?OXn{': 5, 'GOCWrK': 5, 'G@PG\\c': 5, 'GCGHYk': 5, 'GG?^?{': 5, 'G?_pi[': 5, 'GGCWvK': 4, 'GOCOz[': 5, 'G@OI\\k': 5, 'GC?hY{': 5, 'G?DbK{': 4, 'GGCO~[': 4, 'GO?Wz{': 5, 'G@@I\\{': 4, 'GG?W~{': 4, 'G?W[Jc': 5, 'G?YGjc': 5, 'G?ogjc': 5, 'G?`cjo': 5, 'G?`Hpk': 5, 'G?IHis': 5, 'G?_ZbK': 5, 'G?IHqk': 5, 'G?QJ`k': 5, 'G?GXuK': 5, 'G?OZdK': 5, 'G?M@i[': 5, 'G?`PXs': 5, 'GO?YrK': 5, 'G?IPq[': 6, 'GG?YtK': 5, 'G?J@o{': 5, 'GAAJPk': 5, 'G?HSW{': 6, 'G?J?w{': 5, 'G?DcW{': 5, 'G?CkjK': 6, 'G?Cp]K': 5, 'G?ognc': 5, 'G?QHrk': 5, 'G?_ZRk': 5, 'G?O\\Rk': 5, 'G_A_zs': 5, 'G?Y?zk': 5, 'G?WSZk': 5, 'G?oPZk': 5, 'G_?sZs': 5, 'G?OsX{': 5, 'G?Q_x{': 5, 'G_?qX{': 5, 'G?EaX{': 5, 'G?OuH{': 5, 'G?F@X{': 5, 'GA@cX{': 5, 'G?_ZVk': 5, 'G?oP^k': 5, 'G?`_z{': 5, 'G?DcZ{': 5, 'G?F@Z{': 5, 'G?`cj{': 5, 'G?F@^{': 5, 'GCOgZc': 5, 'G@QGZc': 5, 'GGASZo': 5, 'GC@Hp[': 6, 'GC?hq[': 5, 'G_?Z`[': 6, 'G@AHq[': 5, 'GGAJ_{': 4, 'GG?Zc[': 5, 'G@AIW{': 5, 'G?_hik': 6, 'G?C\\JK': 5, 'G@`G^c': 4, 'GOOGzk': 5, 'GG_Gzk': 5, 'G@OKZk': 4, 'GGASZs': 5, 'GC?iX{': 5, 'G?`ah{': 5, 'G@AIX{': 4, 'G@@MH{': 5, 'GG_G~k': 4, 'GC@HZ{': 5, 'G@@KZ{': 4, 'GGASZ{': 4, 'G@AI^{': 4, 'G?LILc': 5, 'G?kOjK': 5, 'G?C\\RK': 5, 'G?C[rK': 5, 'G?F?xs': 4, 'G?[OnK': 4, 'G?PHtk': 5, 'G?C\\b[': 5, 'G?LA\\k': 5, 'GD?Gz[': 5, 'G?Gki{': 5, 'GG?ZK{': 4, 'G?C]H{': 4, 'G?CZf[': 4, 'GB?G~[': 4, 'G?Oq\\{': 5, 'G?C\\J{': 5, 'G?CZN{': 4, 'G@IAyw': 5, 'G@HA{w': 5, 'G@OU\\W': 5, 'G@PD[w': 5, 'G@DA|W': 5, 'GAa@zw': 5, 'G@IAzw': 5, 'G@HCzw': 5, 'GCOTZw': 5, 'G_CTZw': 5, 'G@IAy{': 5, 'G@HA{{': 5, 'G@OU\\[': 5, 'G@PD[{': 5, 'G@DA|[': 5, 'G@IA~w': 5, 'GAa@z{': 5, 'G@IAz{': 5, 'G@HCz{': 5, 'GCOTZ{': 5, 'G_CTZ{': 5, 'G@IA~{': 5, 'G@P@|w': 4, 'G@HA|w': 5, 'GGCa|w': 4, 'G@P@~w': 4, 'G@P@|{': 4, 'G@HA|{': 5, 'GGCa|{': 4, 'G@P@~{': 4, 'GGCa{w': 5, 'GOCayw': 5, 'GB?M\\W': 5, 'G_E@zw': 5, 'GAEDZw': 5, 'GGCczw': 5, 'GOCazw': 5, 'GE?LZw': 5, 'GGCa{{': 5, 'GOCay{': 5, 'GB?M\\[': 5, 'GOCa~w': 5, 'G_E@z{': 5, 'GAEDZ{': 5, 'GGCcz{': 5, 'GOCaz{': 5, 'GE?LZ{': 5, 'GOCa~{': 5, 'G@I@yw': 5, 'GACa|W': 6, 'GGCQ|W': 5, 'G@H@}w': 5, 'GO?wzs': 5, 'G@@Y\\s': 5, 'GG@W|s': 5, 'G@I@y{': 5, 'GACa|[': 6, 'GGCQ|[': 5, 'GG?w~s': 5, 'G@H@}{': 5, 'GO?Xz{': 5, 'G?HQ|{': 5, 'GG?Y|{': 5, 'GG?X~{': 5, 'G?MAzg': 5, 'G?Orsw': 5, 'GAAJpw': 5, 'G?IUZo': 5, 'G@@L]o': 5, 'GCD@~W': 5, 'GC@XZs': 5, 'GAAXZs': 5, 'G@@[Zs': 5, 'G?JKjs': 5, 'GOBGzs': 5, 'G?MAzk': 5, 'G?Ors{': 5, 'GAAJp{': 5, 'G?IUZs': 5, 'G@@L]s': 5, 'GA?kx{': 5, 'GC@Hx{': 5, 'G?_rY{': 5, 'G@@Kx{': 5, 'G?Or[{': 5, 'GG?]X{': 5, 'G?QRX{': 5, 'G@AJY{': 5, 'GG?]l[': 5, 'GAAX^s': 5, 'GCD@~[': 5, 'GC@Hz{': 5, 'GA?kz{': 5, 'GAAHz{': 5, 'G?Qcz{': 5, 'G_?kz{': 5, 'GC@H~{': 5, 'GOCQzW': 5, 'GG?Zsw': 4, 'G@AMZo': 5, 'G_CP~W': 4, 'GO@Wzs': 5, 'GGAWzs': 4, 'GGA[Zs': 4, 'GOCQz[': 5, 'GG?Zs{': 4, 'G@AMZs': 5, 'GG?[x{': 5, 'G_?ZX{': 5, 'GG?Z[{': 4, 'GG?[~K': 4, 'GGAW~s': 4, 'G_CP~[': 4, 'G_?Xz{': 5, 'GG?[z{': 4, 'GGAKz{': 4, 'G_?X~{': 4, 'G@AHzo': 5, 'GB?I|W': 5, 'GGC`}w': 4, 'GA@X\\s': 5, 'G@?{Zs': 4, 'G?DZLs': 5, 'G@AHzs': 5, 'GB?I|[': 5, 'G@?y^s': 4, 'GGC`}{': 4, 'GA?i|{': 5, 'G@AHz{': 4, 'G?Da|{': 4, 'G@@H~{': 4, 'G?_uZo': 5, 'G?Dbsw': 4, 'G?Ebqw': 5, 'GE?H~W': 4, 'G?bHjs': 5, 'G?EZJs': 4, 'G?D\\Js': 5, 'G?_uZs': 5, 'G?Dbs{': 4, 'G?Ebq{': 5, 'G?Op}[': 5, 'G?Dcx{': 5, 'G?F@x{': 4, 'G?EZNs': 4, 'GE?H~[': 4, 'G?`cz{': 5, 'G?Dcz{': 4, 'G?F@z{': 5, 'G?F@~{': 4, 'G@aBzw': 4, 'G@PD~w': 4, 'G@aBz{': 4, 'G@PD~{': 4, 'G@HD}w': 5, 'GO?Zzw': 5, 'GG?\\zw': 5, 'GC?mzw': 5, 'GG?]|w': 5, 'GO?Z~w': 5, 'G@HD}{': 5, 'GO?Zz{': 5, 'GG?\\z{': 5, 'GC?mz{': 5, 'GG?]|{': 5, 'GO?Z~{': 5, 'G@PB|w': 4, 'GG?Z~w': 4, 'G@PB|{': 4, 'GG?Z~{': 4, 'G@@L~o': 4, 'G@@Lzw': 4, 'G@AJzw': 4, 'G?De|w': 4, 'G@AJ~w': 4, 'G@@L~s': 4, 'G@@Lz{': 4, 'G@AJz{': 4, 'G?De|{': 4, 'G@AJ~{': 4, 'GG?^~w': 4, 'GG?^~{': 4, 'G?C[JC': 5, 'G@P@c[': 5, 'GCC`I[': 5, 'G@?sQ[': 5, 'G?oOh[': 5, 'GAO`K{': 5, 'GP?GY{': 5, 'GG?ZC{': 5, 'G?Gka{': 5, 'G?C]@{': 4, 'GI?G\\{': 4, 'G?LAL{': 5, 'G?C\\B{': 4, 'G?CZF{': 4, 'G?Gg}_': 5, 'G_?}@s': 4, 'G?lAHk': 5, 'GF?GX[': 4, 'G?C^BK': 5, 'G?Gg}c': 5, 'G?CW~C': 3, 'G?]CJk': 4, 'GF?GZ[': 4, 'G_B@p{': 4, 'G?PL`{': 5, 'G?C^@{': 4, 'GF?G^[': 3, 'G?aJb{': 4, 'G?C^B{': 4, 'G?C^F{': 3, 'G?CW~K': 3, 'G?CW~[': 3, 'G?CW~{': 3, 'G?C^VG': 4, 'G?CZvG': 4, 'G?`sZs': 4, 'G?F_zs': 4, 'G?C^fW': 3, 'G?C^NK': 3, 'G?C^J[': 5, 'G?C^VK': 4, 'G?CX~K': 4, 'G?CZvK': 4, 'G?F_~s': 3, 'G?aJj{': 4, 'G?C^J{': 4, 'G?C^f[': 3, 'G?C^N{': 3, 'G?LI\\k': 4, 'G?Do~S': 4, 'G?gWzk': 5, 'G?C\\Z[': 5, 'G?C\\j[': 5, 'G?C]X{': 4, 'G?WW~k': 4, 'G?PH|{': 4, 'G?CZn[': 4, 'G?C\\Z{': 5, 'G?CZ^{': 4, 'G?KW~K': 4, 'GCCWz[': 4, 'G@CW~[': 4, 'G?CX~[': 4, 'G?C[z{': 4, 'G?CX~{': 4, 'G?C^^W': 3, 'G?C^nW': 3, 'G?C^Zw': 4, 'G?C^^w': 3, 'G?C^^[': 3, 'G?C^n[': 3, 'G?C^Z{': 4, 'G?C^^{': 3, 'G?C\\zw': 4, 'G?CZ~w': 4, 'G?C\\z{': 4, 'G?CZ~{': 4, 'G?C^~w': 3, 'G?C^~{': 3, 'G?Kta[': 4, 'G?[peK': 4, 'G@I_ys': 5, 'G@SIlK': 5, 'G?KsY[': 5, 'G?QPxw': 5, 'G?ERZW': 5, 'G?Kre[': 4, 'G@G\\I{': 4, 'GACq\\[': 5, 'GBG_}[': 4, 'G?_xq{': 5, 'GO?xq{': 5, 'G?X_{{': 4, 'G@@Yt[': 5, 'G@GZM{': 4, 'G?KsZ{': 4, 'G?TP\\{': 5, 'GG?xu{': 4, 'G?Kq^{': 4, 'G?Src[': 5, 'GAEJPk': 5, 'G?iQZc': 5, 'G@dO^C': 5, 'G?UHhk': 5, 'G?MQXk': 5, 'G?Lak[': 5, 'G?UJ`k': 5, 'G?UPh[': 5, 'G?IYrc': 5, 'G?Lci[': 5, 'GACrS[': 5, 'G?I]Rc': 5, 'G?G{Ys': 5, 'G?QXhs': 5, 'G?_rYw': 5, 'G?C\\ZW': 5, 'G?IYpk': 5, 'G?DR\\W': 5, 'GCOXvK': 5, 'GAEPZ[': 5, 'GCDPZ[': 5, 'G@DSZ[': 5, 'G?f@Zk': 5, 'GCKInK': 5, 'G?QXp{': 5, 'G?XSX{': 5, 'GC@Xr[': 5, 'G?IYp{': 5, 'G?W]H{': 5, 'G@@[r[': 5, 'G?FLRk': 5, 'GAEP^[': 5, 'G?`Xr{': 5, 'G?H[r{': 5, 'G?FLR{': 5, 'G@AYv[': 5, 'G?IYv{': 5, 'GAKrC[': 4, 'GIGXc[': 5, 'G?DrS[': 5, 'G@@is[': 5, 'GALbC{': 4, 'GHH?{{': 4, 'GHCa[{': 5, 'GBGa[{': 4, 'G?HZc{': 5, 'GG@Xs{': 5, 'G?DrS{': 4, 'GHP?|{': 4, 'G?Ozd{': 4, 'G?DrT{': 5, 'G?DrV{': 4, 'GAg[bK': 5, 'GQGXa[': 5, 'GEgOZK': 5, 'G@Aiqs': 5, 'GBCa[[': 5, 'G?DuTS': 5, 'G@@]TS': 5, 'G?IWzc': 5, 'G?EqZS': 5, 'GA@h[s': 5, 'G?Dq\\S': 5, 'G?DelW': 5, 'G?C\\jW': 5, 'GQGXe[': 5, 'GEE@Z[': 5, 'GPCaY{': 5, 'GHCcY{': 5, 'GECLJ[': 5, 'GAcTJ[': 5, 'G?RPp{': 5, 'GAAZP{': 5, 'G?Rcp{': 5, 'G_Aip{': 5, 'G?ErP{': 5, 'G?FRP{': 5, 'GPCa]{': 5, 'G?`\\b{': 5, 'G?Iqr{': 5, 'G?FTR{': 5, 'G?ErV{': 5, 'G@Hc}o': 4, 'G@IZMs': 4, 'G?[sZk': 4, 'G?kqZk': 4, 'G?lKjk': 5, 'GGAxus': 4, 'G?MJjk': 4, 'G?LLjk': 4, 'G@Hc}s': 4, 'GO?zq{': 5, 'GG?|q{': 4, 'GA?|u[': 5, 'G?kq^k': 4, 'G@Ia}{': 4, 'G?MJj{': 4, 'G?LLj{': 4, 'G?dLj{': 5, 'GO?zu{': 4, 'G?MJn{': 4, 'GIO`{w': 4, 'GI?y\\s': 4, 'G?[q\\k': 4, 'G?[ilk': 5, 'GG@yts': 4, 'GIO`{{': 4, 'G?\\Hnk': 4, 'GI@H|{': 4, 'G?LJl{': 4, 'G?WZl{': 5, 'GG@Zt{': 4, 'G?WZn{': 4, 'G@@luo': 5, 'G?EzbS': 5, 'G?Ejjo': 5, 'G?FTZo': 5, 'GHAX]s': 5, 'G?uHjk': 5, 'G?kijk': 5, 'G?[kjk': 5, 'G?n?zk': 5, 'G@AzUs': 5, 'G?Slmk': 5, 'G?W\\jk': 5, 'G?gZjk': 5, 'G?W]lk': 5, 'G@@lus': 5, 'G?O}p{': 5, 'GC?}r[': 5, 'G@@\\r[': 5, 'G@AZr[': 5, 'G?Dmtk': 5, 'G?kink': 5, 'GP?i}{': 5, 'G?ULj{': 5, 'G?W\\j{': 5, 'G?gZj{': 5, 'G?o\\j{': 5, 'G@Aju{': 5, 'G?gZn{': 5, 'G?Ptto': 4, 'G?Ox~_': 4, 'G?IY~_': 5, 'G?Gzmo': 5, 'G?Qxrc': 4, 'G?C}nO': 4, 'G?H\\mo': 5, 'GHPC|w': 4, 'G?bprs': 4, 'G?Rprs': 4, 'G?Jsrs': 5, 'GO@{rs': 4, 'G?Ptts': 4, 'G?Rpvs': 4, 'GHPC|{': 4, 'GO?}r{': 4, 'GG@\\r{': 4, 'G@Amr{': 5, 'GOAZr{': 4, 'GG@\\v{': 4, 'G?Ky^c': 4, 'G?MHzk': 4, 'G?O~`{': 4, 'G?QXx{': 5, 'G?Dj[{': 4, 'G@@Y|[': 5, 'G?LH~k': 4, 'G?_xz{': 4, 'G?HY|{': 5, 'GG?x}{': 4, 'G?Ox~{': 4, 'G?dX^c': 5, 'G?_zq{': 5, 'G?QZp{': 5, 'G?Ozs{': 5, 'G?I]Zs': 5, 'G?_~a{': 5, 'G?`ix{': 5, 'G?IYx{': 5, 'G?FJX{': 5, 'G?Du\\[': 5, 'G?ci~k': 5, 'G?`Xz{': 5, 'G?H[z{': 5, 'G?FLZ{': 5, 'G@AY~[': 5, 'G?IY~{': 5, 'G?Ww~c': 5, 'G?G}q{': 5, 'G?C|Zs': 5, 'G?SZ\\k': 5, 'G?G~a{': 5, 'G?O|q{': 5, 'G?IXzs': 5, 'G?WY|k': 5, 'G?H^`{': 5, 'G?KZ^k': 5, 'G?WX~k': 5, 'G?PX|{': 5, 'G?Ehz{': 5, 'G?DZ\\{': 5, 'G@?z]{': 5, 'G?Dh~{': 5, 'G?Dr^o': 4, 'GG@\\p{': 4, 'G?HZk{': 5, 'G?Dr[{': 4, 'GG@X~s': 4, 'G?Ozl{': 4, 'G?Dr\\{': 5, 'G?Dr^{': 4, 'G?ow~c': 4, 'G?cZZk': 4, 'G?_}Zs': 4, 'G?WZk{': 4, 'G?gYzk': 5, 'G?Dnc{': 4, 'G?Dkx{': 5, 'G?FHx{': 4, 'G?cZ^k': 4, 'G?oX~k': 4, 'G?`kz{': 4, 'G?Dkz{': 4, 'G?FHz{': 5, 'G?FP~[': 4, 'G?FH~{': 4, 'G?Er^o': 5, 'G@@ms{': 5, 'G@@Zt[': 5, 'G?C|j[': 5, 'G?Dq|[': 5, 'G@Ai~s': 5, 'G?`\\j{': 5, 'G?Iqz{': 5, 'G?FTZ{': 5, 'G?Er^{': 5, 'G?W^ng': 4, 'GG?~uw': 4, 'G?W^nw': 4, 'G?W^nk': 4, 'GG?~u{': 4, 'G?W^n{': 4, 'G?LL~g': 4, 'G?Qx~s': 4, 'G?LL~k': 4, 'G?_zz{': 4, 'G?O|z{': 4, 'G?O|~k': 4, 'G?_z~{': 4, 'G?WZ~g': 4, 'G?Px~s': 4, 'G?WZ~k': 4, 'GG?z}{': 4, 'G?Oz~{': 4, 'G?H\\~o': 5, 'G?Iy~s': 5, 'G?H\\~s': 5, 'G?_}z{': 5, 'G?H\\z{': 5, 'G?IZz{': 5, 'G?Dm|{': 5, 'G@@\\~[': 5, 'G?IZ~{': 5, 'G?Rp~s': 4, 'GG@\\|{': 4, 'GG@\\~{': 4, 'G?O~~w': 4, 'G?O~~{': 4, 'G@G[rG': 5, 'GAgpa[': 5, 'GOKqa[': 5, 'GChOrK': 5, 'GQ_WrK': 5, 'GO?yqs': 5, 'GHCQ[[': 5, 'G?`pps': 5, 'G?]Ahk': 5, 'GAAips': 6, 'GGAYps': 5, 'G?`rSs': 5, 'G@BLQs': 5, 'G?_Xzg': 5, 'GGAWxs': 5, 'G?`qXs': 5, 'GC@iXs': 5, 'G?FbO{': 5, 'GG@X[s': 5, 'G?CmnG': 5, 'GCKrE[': 5, 'GDGaY{': 5, 'GBGcY{': 5, 'GCSTJ[': 5, 'GcCPZ[': 5, 'GHI?y{': 5, 'GPH?y{': 5, 'GDOSZ[': 5, 'GQCSZ[': 5, 'G?_z`{': 5, 'GC@ZP{': 5, 'G_@Xp{': 5, 'G?JQp{': 5, 'GG@[p{': 5, 'G?FeP{': 5, 'GAAmP{': 5, 'GDGa]{': 5, 'GPH?}{': 5, 'GO?yr{': 5, 'G?Qpr{': 5, 'G?JSr{': 5, 'GO@[r{': 5, 'G?_zf{': 5, 'G_Kpa[': 4, 'GK_WrK': 4, 'GQCQX[': 5, 'G@BHuS': 4, 'GC@jO{': 5, 'G?C^NG': 3, 'G_Kpe[': 3, 'G`G_y{': 4, 'GKCSZ[': 4, 'GO@Yp{': 5, 'G@BMP{': 4, 'G`G_}{': 3, 'G_?xr{': 4, 'GGA[r{': 4, 'G_?xv{': 3, 'GB_[RK': 5, 'GEGha[': 5, 'GCwOjK': 4, 'GASHlK': 6, 'G?aZRc': 5, 'G@?}US': 4, 'G@KHmK': 4, 'G?CyvC': 5, 'G@BHps': 4, 'G?Faps': 5, 'G?JOxs': 5, 'G?FaXs': 6, 'GG@g{s': 5, 'G?DfKw': 4, 'G?CX~G': 4, 'GEGhe[': 4, 'GCcRJ[': 5, 'G@KeI{': 5, 'GCC^B[': 4, 'GBECZ[': 5, 'GWC_y{': 5, 'GF?KZ[': 4, 'GA@\\P{': 6, 'G?QuP{': 5, 'G_?}P{': 4, 'G@?}P{': 4, 'G?D^@{': 5, 'G@KeM{': 4, 'GWC_}{': 4, 'G?`sr{': 5, 'G@?}R{': 5, 'G?Fcr{': 4, 'G@?}V{': 4, 'G?]Bjg': 4, 'G?`tro': 5, 'G_?|ro': 4, 'G?_zjo': 5, 'G_?xzo': 4, 'G?G}mo': 5, 'GGAY|o': 5, 'GIQ@|w': 4, 'G_@xrs': 4, 'GGA{rs': 5, 'G_Axrs': 4, 'G?]Bjk': 4, 'G?`trs': 5, 'G_?|rs': 4, 'G_@xvs': 4, 'GIQ@|{': 4, 'G_?zr{': 4, 'G?Qtr{': 5, 'G_?|r{': 4, 'G_?zv{': 4, 'GGAZro': 4, 'G@BLro': 4, 'G?Qpzo': 5, 'G?I]jo': 5, 'GGA[zo': 4, 'G@?zuW': 4, 'G?C}vG': 4, 'G`P@|w': 4, 'GOAyrs': 5, 'GG@{rs': 4, 'G@A}Rs': 4, 'GGAZrs': 4, 'G@BLrs': 4, 'GG@{vs': 4, 'G`P@|{': 4, 'GO@\\r{': 5, 'GGAZr{': 4, 'G@BLr{': 4, 'GGAZv{': 4, 'G?_zno': 5, 'GG?zs{': 5, 'GO?}q{': 5, 'GO@Zp{': 5, 'GGAZp{': 5, 'GC@mp{': 5, 'G_?|q{': 5, 'G?_xzk': 5, 'G?`qx{': 5, 'GA@X|[': 5, 'GG@X{{': 5, 'G?FeX{': 5, 'G@Ai}[': 5, 'GO?y~s': 5, 'GO@X~s': 5, 'GO?yz{': 5, 'G?Qpz{': 5, 'G?JSz{': 5, 'GO@[z{': 5, 'G?_zn{': 5, 'G_?x~o': 3, 'G_?zp{': 4, 'G_?}p{': 4, 'GO@Yx{': 5, 'G@?}][': 4, 'G_?x~s': 3, 'G_?xz{': 4, 'GGA[z{': 4, 'G_?x~{': 3, 'G@?}^o': 4, 'G@?}u[': 5, 'G@?zu[': 4, 'G?C}vK': 4, 'GC@js{': 5, 'G@BJp{': 4, 'G?Fep{': 4, 'G@?x}[': 4, 'G?DX~K': 4, 'G@?}^s': 4, 'G@BH~s': 4, 'G?`sz{': 5, 'G@?}Z{': 4, 'G?Fcz{': 4, 'G@?}^{': 4, 'G_?~vo': 3, 'G_?~vw': 3, 'G_?~vs': 3, 'G_?~v{': 3, 'G_?~rw': 4, 'G_@x~s': 4, 'G_?~r{': 4, 'G_?zz{': 4, 'GO@\\z{': 5, 'G_?|z{': 4, 'G_?z~{': 4, 'GGA^rw': 4, 'GG@{~s': 4, 'GGA^r{': 4, 'GGAZz{': 4, 'G@BLz{': 4, 'GGAZ~{': 4, 'G_?~~w': 3, 'G_?~~{': 3, 'GBOG|K': 5, 'G@SpUK': 5, 'GAKIlK': 5, 'G@Ahqs': 5, 'GBCI\\K': 5, 'G?MQh[': 5, 'G?MOzK': 5, 'G?C|bS': 5, 'G?SZdK': 5, 'G?IYhs': 5, 'G?FBXw': 5, 'G?EPzW': 5, 'GGKPm[': 5, 'G@DQ\\[': 5, 'GOGXi{': 5, 'GB?Y\\[': 5, 'GHGO}[': 5, 'GADP\\[': 5, 'G@GsY{': 5, 'GAD_|[': 5, 'G@Kam[': 5, 'G?IXq{': 5, 'G?XHk{': 5, 'GA@Xt[': 5, 'G?gXi{': 5, 'G@?|Q{': 5, 'G?Dqt[': 5, 'GGGXm{': 5, 'G@Gq]{': 5, 'G?THl{': 5, 'G?Kkj{': 5, 'G?SZL{': 5, 'G@?zU{': 5, 'G?Kin{': 5, 'GECg^C': 4, 'G?dRH[': 5, 'G?KuI[': 5, 'G?_}Rc': 5, 'G?oXhk': 4, 'G?YOxk': 5, 'G?Ejas': 5, 'GB?ZS[': 4, 'G?LeG{': 6, 'G?N?xk': 4, 'G?cXjK': 6, 'G?EZbS': 5, 'G?Kg}K': 5, 'G?G\\Yw': 6, 'G?DeXw': 5, 'G?Db[w': 5, 'G?oWxk': 4, 'G?FHhs': 5, 'G?EXjS': 5, 'GEGG~K': 4, 'G?NCZk': 4, 'GE?XZ[': 5, 'GB?[Z[': 4, 'GECH^K': 4, 'G?dcZk': 5, 'G@F?z[': 5, 'GCD_z[': 5, 'GCCZVK': 4, 'G?XKh{': 5, 'G?LMH{': 5, 'G?`krk': 5, 'G?oXh{': 4, 'G?gYh{': 5, 'G?FPr[': 5, 'G?Dsr[': 4, 'GE?X^[': 4, 'G@F?~[': 4, 'G?NCZ{': 4, 'G?oXj{': 5, 'G?W[j{': 4, 'G?FPv[': 4, 'G?oXn{': 4, 'G?F@xw': 4, 'G?Kpm[': 4, 'G@Cp][': 4, 'G@GW}[': 4, 'G?Cxu[': 4, 'G@?xu[': 4, 'G@Gg}{': 4, 'G?Gxu{': 4, 'G?Cxu{': 4, 'G?Cxv{': 4, 'G?So~C': 5, 'G?G[yw': 5, 'G?EXrK': 5, 'GAGW~K': 5, 'G?SXnK': 5, 'GCGWz[': 5, 'G@_Wz[': 5, 'G?cXj[': 5, 'G?DXvK': 5, 'G?EYp{': 5, 'G@OW~[': 5, 'G?DXv[': 5, 'GCCXZ{': 5, 'G?DXv{': 5, 'G?C~fO': 4, 'G@JP]s': 4, 'G?]Kjk': 4, 'G?shjk': 5, 'G?w[jk': 4, 'G?Jpus': 4, 'G?Kmmk': 4, 'G?KZnK': 5, 'G?K]nK': 4, 'G?C~fS': 4, 'G?aZZs': 4, 'G?Kh}k': 4, 'G?D^P{': 5, 'G?C~e[': 4, 'G?shnk': 4, 'G@Gu]{': 4, 'G?eJj{': 4, 'G?Kmj{': 5, 'G?c^J{': 4, 'G@?~U{': 4, 'G?Kmn{': 4, 'G@Sh]k': 4, 'G?[hmk': 5, 'GDCXZ[': 4, 'GBCY\\[': 4, 'G@C\\Z[': 4, 'G@C]Z[': 5, 'G?K]Zk': 5, 'G?C{zs': 4, 'GBCX^[': 4, 'G@Gi}{': 4, 'G?Gzu{': 5, 'G@C\\Z{': 4, 'GACZ\\{': 4, 'G@CZ^{': 4, 'G@oW~K': 4, 'G?sXnK': 4, 'GECXZ[': 5, 'GBC[Z[': 4, 'GCCZZ[': 4, 'GECX^[': 4, 'GCCZ^[': 4, 'G?cZn[': 4, 'GAC\\Z{': 5, 'GCCZZ{': 4, 'GCCZ^{': 4, 'G@KW~K': 4, 'G?C}p{': 4, 'G@CX~[': 4, 'G?Gx}{': 4, 'G?Cx}{': 4, 'G?Cx~{': 4, 'GAKW~K': 4, 'G?EXzs': 5, 'G?EYx{': 4, 'GACX~[': 4, 'G?DX~[': 5, 'G?EXz{': 4, 'G?DX~{': 4, 'G@C^^W': 4, 'G?C}~o': 4, 'G@C^^w': 4, 'G@C^^[': 4, 'G?C}~s': 4, 'G@C^^{': 4, 'G?C~^o': 4, 'G?Fh~s': 4, 'G?C~^s': 4, 'G?G}}{': 4, 'G?C~Z{': 5, 'G?C}~[': 4, 'G?C~n[': 4, 'G?G}~{': 4, 'G?C~rw': 4, 'G?Dx~s': 4, 'G?C~r{': 4, 'G?C|z{': 4, 'G?C}z{': 4, 'G?Cz~{': 4, 'G?FX~s': 4, 'G?EZz{': 4, 'G?EZ~{': 4, 'G?C~~w': 4, 'G?C~~{': 4, 'G?`zv_': 3, 'G?\\s^c': 3, 'G?]Jjk': 3, 'G?`zvc': 3, 'G?_zzw': 4, 'G?`rzw': 4, 'G?J]p{': 4, 'G?Pt|w': 4, 'G?]Jnk': 3, 'G?`zr{': 3, 'G?Q|r{': 4, 'G_@zt{': 3, 'G?`zv{': 3, 'G?xo~c': 4, 'G?P|ts': 4, 'G?\\Jlk': 4, 'G?D~fS': 4, 'G?`|rs': 4, 'G?Qzrs': 4, 'G?J\\rs': 3, 'GGAzus': 4, 'G?Qxzs': 4, 'G?J[zs': 5, 'G?Qtzw': 5, 'G?Fhzs': 5, 'GG@y|s': 4, 'G?Fkzs': 4, 'G@Az]s': 5, 'G?[^Nk': 4, 'G?wZnk': 4, 'G?azr{': 4, 'G?Fjr{': 4, 'G?I}r{': 3, 'GG@}t{': 4, 'G?Fjv{': 4, 'G?D~fO': 4, 'G?FvVo': 3, 'G_Azrs': 3, 'G?O|~g': 4, 'G_?|zw': 4, 'G?C~nW': 4, 'G_Azvs': 3, 'G?`~b{': 3, 'G?FvR{': 4, 'G?FvV{': 3, 'G?`~vo': 3, 'G?`z~o': 3, 'G?Fj~o': 4, 'G?Fv^o': 3, 'G?bzvs': 3, 'G?`~vs': 3, 'G_@~t{': 3, 'G?`~v{': 3, 'G?`~r{': 3, 'G?`zz{': 3, 'G?Q|z{': 4, 'G?`z~k': 3, 'G?`z~{': 3, 'G?P~t{': 4, 'G?Q~r{': 4, 'G?Fjz{': 4, 'G?Flz{': 3, 'G?Fj~{': 4, 'G?D~n[': 4, 'G?Fv^{': 3, 'G?`~~{': 3, 'GBWW~K': 4, 'G?Ejzw': 5, 'GG@zs{': 4, 'G?Dzs{': 4, 'GBCZ^[': 4, 'G?Pzt{': 4, 'G?Dzt{': 4, 'G?Dzv{': 4, 'GDWW~K': 4, 'G?H|us': 3, 'G?Ezrs': 4, 'G?D|rs': 4, 'G?D}ts': 4, 'G?Dlzw': 5, 'G?Dm|w': 5, 'G@Azu[': 4, 'G?C|zw': 4, 'G?Dy|s': 4, 'GDCZ^[': 4, 'G?Izu{': 3, 'G?Ezr{': 4, 'G?F\\r{': 4, 'G?Ezv{': 4, 'G?D~vo': 4, 'G?Dz~o': 4, 'G?Ez~o': 4, 'G?Fzvs': 4, 'G?D~vs': 4, 'G?D~v{': 4, 'G?D~r{': 4, 'G?Ezz{': 4, 'G?Dz~{': 4, 'G?D~t{': 4, 'G?F\\z{': 4, 'G?Ez~{': 4, 'G?D~~{': 4, 'G?F~vo': 3, 'G?F~vs': 3, 'G?Fn~w': 3, 'G?D~~w': 4, 'G?F~v{': 3, 'G?F~~{': 3, 'G?db?k': 5, 'G?ou@c': 5, 'G?Ko]C': 4, 'GB@_[S': 5, 'G@GW]C': 5, 'GC`b?{': 4, 'GP@IO{': 5, 'GK`@G{': 5, 'G?Xc_{': 4, 'GW?]?{': 5, 'G?op_{': 4, 'GGOk_{': 5, 'GIAKP{': 4, 'GgCOX{': 5, 'G?NE@{': 4, 'G?TT@{': 4, 'G_MAH{': 5, 'G@G]@{': 4, 'GoCOZ{': 4, 'G?YSb{': 4, 'G@G]B{': 4, 'G@G]F{': 4, 'G?NMPk': 4, 'G?KxuK': 4, 'G@G]vG': 4, 'G?Y[rk': 4, 'G?oxrk': 4, 'G@J_}s': 4, 'G?Ku][': 4, 'G?TTX{': 5, 'G@Cmm[': 4, 'G?Kp}[': 4, 'G@GY~K': 4, 'G@G]vK': 4, 'G?oxvk': 4, 'G?eRZ{': 4, 'G?KuZ{': 4, 'G@G^M{': 4, 'G?Ku^{': 4, 'G?gqyw': 5, 'G@DYt[': 4, 'G?Wxuk': 5, 'GCCxr[': 5, 'G@Wg}k': 4, 'G?Ksy{': 4, 'G?KtY{': 5, 'G@G\\Y{': 4, 'GACxv[': 4, 'G?TP|{': 4, 'G?Kr]{': 4, 'G?Ksz{': 4, 'G@GZ]{': 4, 'G?Kq~{': 4, 'G@G^eW': 4, 'GCYGzk': 4, 'G@F`]s': 4, 'G@ogzk': 5, 'G@G]Y{': 5, 'G@G]][': 4, 'G@G]m[': 4, 'G@GZm[': 5, 'G@G^e[': 4, 'G@GX}[': 4, 'G@og~k': 4, 'GC_ZZ{': 4, 'G@CnM{': 4, 'G@G]Z{': 5, 'G@G]^{': 4, 'G@Cxu[': 4, 'G@Kp]{': 4, 'G?Kp}{': 4, 'G@GX~{': 4, 'G?eRzw': 4, 'G?Kv]w': 4, 'G?Kuzw': 4, 'G@G^]w': 4, 'G?Ku~w': 4, 'G?eRz{': 4, 'G?Kv]{': 4, 'G?Kuz{': 4, 'G@G^]{': 4, 'G?Ku~{': 4, 'G@G\\zw': 4, 'G@GZ~w': 4, 'G@G\\z{': 4, 'G@GZ~{': 4, 'G@G^~w': 4, 'G@G^~{': 4, 'G?LacK': 5, 'GGDPSK': 5, 'G?XPc[': 5, 'GB@HS[': 5, 'G@Oic[': 5, 'G?SrC{': 5, 'GGDPS{': 5, 'GAL@K{': 5, 'G?Lad{': 5, 'GIGO^{': 5, 'GqGOOK': 6, 'GG`PGs': 6, 'G_G\\Ac': 6, 'GQ?HWw': 6, 'GGd@Gk': 6, 'G?hU@c': 6, 'GCKHIK': 6, 'GA``Gs': 6, 'GAL@KK': 6, 'G@P_kS': 6, 'G?SuDC': 6, 'GDGGYK': 6, 'GCGWZC': 6, 'G?daHc': 6, 'GH@GkS': 6, 'G@?kYo': 6, 'GGHOkS': 6, 'G??|Qo': 6, 'GCQb?{': 6, 'G`OHG{': 6, 'GI_cG{': 6, 'G_W_g{': 6, 'G@QJ?{': 6, 'GW_QG{': 6, 'GG`T?{': 6, 'GKCHG{': 6, 'GWOGg{': 6, 'G_Oh_{': 6, 'GHOKG{': 6, 'G@p@G{': 6, 'GGQT?{': 6, 'GCOpO{': 6, 'GGo_g{': 6, 'GGQH_{': 6, 'GWAQO{': 6, 'G?cr?{': 6, 'G?p`_{': 6, 'GQAIP{': 6, 'GAIM@{': 6, 'GaCHH{': 6, 'GICKH{': 6, 'GcGIH{': 6, 'GAiAH{': 6, 'GAd@H{': 6, 'G_EaP{': 6, 'G?Ma`{': 6, 'GEOHH{': 6, 'GAEJ@{': 6, 'G?hU@{': 6, 'GQCKJ{': 6, 'GAISR{': 6, 'GPCIJ{': 6, 'G@FCR{': 6, 'G?Maf{': 6, 'GBGZC[': 5, 'GBO_{[': 5, 'GBGJK{': 5, 'GHD@[{': 5, 'GIL@K{': 5, 'GAGZK{': 5, 'GGDP[{': 5, 'G@PP[{': 5, 'GIGQ\\{': 5, 'G@Oil{': 5, 'GGDP^{': 5, 'G?\\PcK': 5, 'G@`JSg': 5, 'GAKYLC': 5, 'GGSXcK': 5, 'G?DXv?': 5, 'G?FLR_': 5, 'G@dU@[': 5, 'GOLR?{': 5, 'GdCIH[': 5, 'GB`K`[': 5, 'G`EI`[': 5, 'GXCIG{': 5, 'GPHQO{': 5, 'GFAIP[': 5, 'GBEM@[': 5, 'GBOc[[': 5, 'GIC_{[': 5, 'GGMTA{': 5, 'G_La`{': 5, 'GXCKI{': 5, 'GHISQ{': 5, 'GE`@X{': 5, 'GBHCX{': 5, 'GcCJH{': 5, 'GCUBH{': 5, 'GcD@X{': 5, 'GHCMH{': 5, 'GIGSX{': 5, 'G?dV@{': 5, 'GE_JH{': 5, 'G_Lad{': 5, 'GDIAZ{': 5, 'GBOcZ{': 5, 'GPCMJ{': 5, 'GSGQZ{': 5, 'GBOc^{': 5, 'G@DItK': 5, 'GAL?|K': 5, 'G?M`is': 5, 'G@[_mK': 5, 'G@G\\a[': 5, 'G?TPl[': 5, 'GBGHm[': 5, 'GAOo|[': 5, 'G?KtI{': 5, 'G@GZe[': 5, 'G@PO|[': 5, 'GGOg{{': 5, 'G@_gy{': 5, 'GOCpY{': 5, 'G?KrM{': 5, 'GAOX\\{': 5, 'GGCp]{': 5, 'G@G[Z{': 5, 'G@GY^{': 5, 'G@Lac[': 5, 'GBKaK[': 5, 'GJ?gs[': 5, 'G@Da[[': 5, 'GBH@[{': 5, 'GGSrC{': 5, 'GIC`[{': 5, 'GHCJK{': 5, 'G@SbK{': 5, 'GGOXk{': 5, 'G@HQ[{': 5, 'G?LRK{': 5, 'G?XPk{': 5, 'GBHA\\{': 5, 'GAOp\\{': 5, 'G?Wql{': 5, 'G?Lal{': 5, 'G?Lan{': 5, 'GAKqSK': 5, 'G?h]@c': 5, 'GAMSRK': 5, 'G@HS]S': 5, 'G@HQs[': 5, 'GRGGi[': 5, 'GAkSJK': 5, 'G@Eaq[': 5, 'G@Das[': 5, 'G?LUTK': 5, 'G@G[i[': 5, 'GAe@j[': 5, 'GR?gu[': 5, 'GPCJI{': 5, 'GE_Hj[': 5, 'GHCLI{': 5, 'GAELb[': 5, 'GAQPX{': 5, 'G_Q_x{': 5, 'GAF@X{': 5, 'G?Mah{': 5, 'G?URH{': 5, 'G?qah{': 5, 'GPCJM{': 5, 'GC`PZ{': 5, 'G@EaZ{': 5, 'G?dTJ{': 5, 'G?Man{': 5, 'G@aRZo': 5, 'GAHbsw': 5, 'GODsZs': 5, 'GAJ_zs': 5, 'G@b_zs': 5, 'GIGU\\w': 5, 'GAHc{{': 5, 'GGDLh{': 5, 'G@aRZs': 5, 'GAHbs{': 5, 'GAJ_~s': 5, 'G@aaz{': 5, 'GAHcz{': 5, 'GOCuZ{': 5, 'GIGU\\{': 5, 'GAHc~{': 5, 'GGSbkw': 5, 'GAKi\\k': 5, 'GGDq\\s': 5, 'GAWg|k': 5, 'G@Si\\k': 5, 'GB@i\\s': 5, 'GGO\\h{': 5, 'GGSbk{': 5, 'G@Si^k': 5, 'GAHH|{': 5, 'G@Pa|{': 5, 'GGGY|{': 5, 'G@HI|{': 5, 'GH@I|{': 5, 'GAHH~{': 5, 'G@DduW': 5, 'GOUGzk': 5, 'G@Qp]s': 5, 'GAggzk': 5, 'GCWgzk': 5, 'G@qGzk': 5, 'GD@h]s': 5, 'GOCmi{': 5, 'GGGY{{': 5, 'GOGYy{': 5, 'GGO[|k': 5, 'G@O\\j[': 5, 'GAG]l[': 5, 'G@Ddu[': 5, 'GCGXz[': 5, 'G@O]X{': 5, 'GH?[z[': 5, 'GOGYzk': 5, 'GCCmj[': 5, 'GAgg~k': 5, 'G__Xz{': 5, 'GCGr]{': 5, 'GGG[z{': 5, 'GOGYz{': 5, 'GA_\\Z{': 5, 'GD?j]{': 5, 'GOGY~{': 5, 'G?Ldmo': 5, 'GCLKZk': 5, 'GGEp]s': 5, 'G@ciZk': 5, 'GChGzk': 5, 'G@SkZk': 5, 'G?MrMs': 5, 'G@Omk{': 5, 'G@Oi{{': 5, 'G@O]\\[': 5, 'G@_iy{': 5, 'GAOlk{': 5, 'G@O\\Zk': 5, 'G@O]l[': 5, 'G@_Zj[': 5, 'G?Ldms': 5, 'G@O\\Y{': 5, 'G@IHy{': 5, 'G@DJl[': 5, 'GAClm[': 5, 'G@EJj[': 5, 'G@ci^k': 5, 'GCQHz{': 5, 'GOCr]{': 5, 'G@HKz{': 5, 'GCO\\Z{': 5, 'G@IIz{': 5, 'G@Eb]{': 5, 'G@II~{': 5, 'G?iRrg': 5, 'GO`ozs': 5, 'GBHE\\w': 5, 'GGJOzs': 5, 'GOJOzs': 5, 'G@FcZs': 5, 'GD@kZs': 5, 'GI?k{{': 5, 'G?iRrk': 5, 'GB@LX{': 5, 'GGJO~s': 5, 'GS?iz{': 5, 'GBHE\\{': 5, 'GI?kz{': 5, 'GP?]Z{': 5, 'G@EeZ{': 5, 'GPAIz{': 5, 'GI?k~{': 5, 'G?hQxw': 5, 'GGKg}k': 5, 'G@Ki]k': 5, 'G@cXj[': 5, 'GASXl[': 5, 'G?Lhuk': 5, 'G@OX~K': 5, 'GH?X}[': 5, 'G@DNH{': 5, 'G?M`y{': 5, 'G?SuX{': 5, 'G@SXn[': 5, 'GGGX}{': 5, 'G@HH}{': 5, 'GCChz{': 5, 'GACi|{': 5, 'G?Wp}{': 5, 'GACh~{': 5, 'GGPo|s': 5, 'G?Wytk': 5, 'G?Litk': 5, 'G?Livk': 5, 'GI?i|{': 5, 'G?Wq|{': 5, 'G?XP|{': 5, 'G?XP~{': 5, 'G?XXsk': 5, 'G?XXks': 5, 'G@UG~K': 5, 'GCDXr[': 5, 'G@S[j[': 5, 'G?MYvK': 5, 'GAG[~K': 5, 'G@OZ[{': 5, 'GCOZX{': 5, 'G@_ZY{': 5, 'GCCnI{': 5, 'GACkx{': 5, 'G?Sr[{': 5, 'G?dPx{': 5, 'G?URX{': 5, 'G@EYv[': 5, 'GA_X~[': 5, 'G?Ssz{': 5, 'GAEHz{': 5, 'G?dP~[': 5, 'G?dP~{': 5, 'G@HLmo': 5, 'G?K|Qk': 5, 'G?VLPk': 5, 'GGIo}s': 5, 'G@Iq]s': 5, 'G?gyrk': 5, 'G?W{rk': 5, 'G?h[rk': 5, 'G?NKrk': 5, 'G@HLms': 5, 'GGG\\i{': 5, 'GB?k}[': 5, 'G@DLj[': 5, 'G?Lek{': 5, 'G?Wq{{': 5, 'G?gqy{': 5, 'G?Su\\[': 5, 'G?gyvk': 5, 'GP?Z]{': 5, 'G@IR]{': 5, 'G?Wsz{': 5, 'G?gqz{': 5, 'G?UTZ{': 5, 'G?qPz{': 5, 'G?gq~{': 5, 'GAHL|w': 5, 'GAG^nW': 5, 'GAHJ|w': 5, 'GGG]~g': 5, 'GAHL~w': 5, 'GAHL|{': 5, 'GAG^n[': 5, 'GAHJ|{': 5, 'GGG]~k': 5, 'GAHL~{': 5, 'G?XR|w': 5, 'G?Sr~w': 5, 'G?XR|{': 5, 'G?Sr~{': 5, 'GAG\\~W': 5, 'G@HL}w': 5, 'GAClzw': 5, 'GCCjzw': 5, 'G?dTzw': 5, 'G?Ld}w': 5, 'GCCj~w': 5, 'GAG\\~[': 5, 'G@HL}{': 5, 'GAClz{': 5, 'GCCjz{': 5, 'G?dTz{': 5, 'G?Ld}{': 5, 'GCCj~{': 5, 'G?XT|w': 5, 'G?XT~w': 5, 'G?XT|{': 5, 'G?XT~{': 5, 'G?Sv~w': 5, 'G?Sv~{': 5, 'GQOWpK': 5, 'GBOc[W': 5, 'G`OkOk': 6, 'GWCWqK': 5, 'G@G]UG': 5, 'G@TO\\C': 5, 'GIKO[K': 6, 'GBDG\\C': 5, 'GBWO[K': 5, 'G?`kr_': 5, 'GGeQ`[': 5, 'G_Kr?{': 5, 'Gk?Wp[': 5, 'GKEI`[': 5, 'G@db?{': 5, 'GAeR@[': 5, 'GacPH[': 6, 'GGKu?{': 5, 'GHcaG{': 5, 'GEEJ@[': 5, 'GEoPH[': 5, 'GQO_w{': 5, 'GBaAX[': 5, 'GQGSY[': 6, 'GWCOy[': 5, 'GOS_yk': 5, 'GBAI\\S': 5, 'G@F@]S': 5, 'GAQ`o{': 5, 'GHAIo{': 6, 'G@JCYs': 6, 'GBAKZS': 5, 'G?Ub_{': 5, 'GBAJO{': 5, 'G?YSZc': 5, 'G_KtA{': 5, 'GDgaI{': 5, 'GBXCH{': 5, 'GOKuA{': 5, 'GPcaI{': 5, 'GK`?x{': 5, 'G`H?x{': 5, 'GgCSX{': 5, 'GKDCX{': 5, 'GPP?x{': 5, 'GC`ap{': 5, 'Gc?ip{': 6, 'GEGaX{': 5, 'GQGQX{': 5, 'GCDeP{': 5, 'GE?mP{': 5, 'GBXCL{': 5, 'G`I?z{': 5, 'GS@Hr{': 5, 'GQO_z{': 5, 'G@JCr{': 5, 'GP@Kr{': 5, 'GQO_~{': 5, 'GoCWrK': 4, 'G@KuA[': 4, 'GCd_rK': 5, 'G@J@o{': 4, 'G?ouPk': 5, 'GD@IX[': 5, 'G?NEHk': 4, 'G?dbG{': 4, 'GoCOz[': 4, 'G@KuE[': 4, 'GEG`Y{': 4, 'GCWSj[': 5, 'Gg?Wx{': 5, 'GS@IX{': 4, 'G?oph{': 4, 'G?hQh{': 4, 'G?NEH{': 4, 'GEG`]{': 4, 'Go?Wz{': 4, 'G?opj{': 4, 'GBAKZ{': 4, 'G?opn{': 4, 'G@G\\aW': 6, 'G?qi`c': 6, 'GQC[RK': 5, 'GB@K\\S': 5, 'GH?Ys[': 5, 'GBIHa[': 5, 'GAc\\BK': 5, 'GPKQI[': 6, 'GDd?ZK': 6, 'GB?is[': 5, 'G?SuTK': 5, 'GGIOw{': 5, 'GCDaX[': 5, 'GB@H[[': 5, 'G?NDIk': 5, 'G@FAX[': 6, 'G?hPpk': 6, 'GBAIp[': 6, 'G?hUPk': 6, 'GAEap[': 5, 'G_cPj[': 5, 'GDKaM[': 5, 'G@cbI{': 5, 'GCoPj[': 5, 'G@SdI{': 5, 'GCO\\b[': 5, 'GQE?z[': 5, 'Ga?XX{': 5, 'Gc?iX{': 5, 'GI?[X{': 5, 'GAQcX{': 5, 'GKC`Y{': 5, 'G@oSj[': 5, 'GQC`Y{': 6, 'GDOKj[': 6, 'GE@HX{': 5, 'G?gqh{': 5, 'G?dRH{': 5, 'G?XSh{': 5, 'G?UeH{': 5, 'G?LUH{': 6, 'G@cbM{': 5, 'GO`Oz{': 5, 'GKC`]{': 5, 'GD?iZ{': 5, 'G?hSj{': 5, 'G?U`j{': 5, 'G@FCZ{': 5, 'G?gqn{': 5, 'G?NM@c': 4, 'G@Ko]C': 4, 'G?]SbK': 4, 'G@G]UK': 5, 'GAOXtK': 5, 'GBcKJK': 4, 'GF?hQ[': 5, 'G?KuUK': 4, 'GADHtK': 5, 'G@GXuK': 4, 'G@GW}K': 4, 'G?NEPk': 4, 'GAE`q[': 5, 'G?eRb[': 4, 'GF?hU[': 4, 'GCEJb[': 4, 'G?KvA{': 5, 'GBa?z[': 4, 'G_OsX{': 5, 'GAO\\H{': 5, 'GB_Kj[': 4, 'GWCPY{': 5, 'G?ouH{': 4, 'G?TTH{': 5, 'G?KuH{': 4, 'G?KvE{': 4, 'GC`_z{': 4, 'GWCP]{': 4, 'G?dcj{': 4, 'G?KuJ{': 5, 'G?KuN{': 4, 'GSP@xw': 4, 'G`I@yw': 5, 'GBa@zW': 4, 'G@J@}o': 4, 'G?hP~_': 4, 'GIa@zw': 4, 'GQOczw': 4, 'GSP@x{': 4, 'G`I@y{': 5, 'GBa@z[': 4, 'G@J@}s': 4, 'G?hP~c': 4, 'GSP@~w': 4, 'GIa@z{': 4, 'GQOcz{': 4, 'GSP@~{': 4, 'GIAJpw': 5, 'G@JDqw': 5, 'G?hTrg': 6, 'Go?wzs': 5, 'GPPA|w': 5, 'GW@Wzs': 5, 'GWAWzs': 5, 'GBAkZs': 5, 'Gg?Xx{': 5, 'GW?[y{': 5, 'GIAJp{': 5, 'G@JDq{': 5, 'G?hTrk': 6, 'GW?Xy{': 5, 'GP@Hy{': 5, 'GE?kz[': 5, 'G?dbk{': 5, 'GW@W~s': 5, 'Go?Xz{': 5, 'GPPA|{': 5, 'Gg?Xz{': 5, 'G?otj{': 5, 'G?Udj{': 5, 'Gg?X~{': 5, 'G?hRtg': 4, 'GS?yZs': 4, 'G`HA|w': 4, 'GDAiZs': 4, 'GB@kZs': 4, 'G?MuJs': 4, 'Ga?kx{': 5, 'GIAHx{': 4, 'GC`ax{': 4, 'G?hRtk': 4, 'GE?mX{': 4, 'GBAHz[': 4, 'G?da|k': 4, 'G@J@y{': 5, 'GB@k^s': 4, 'GS@Hz{': 4, 'G`HA|{': 4, 'GP@Kz{': 4, 'GIAHz{': 4, 'G@JCz{': 4, 'GIAH~{': 4, 'G?o}Pk': 4, 'GW?w}s': 4, 'G@G}Ms': 4, 'G?K}Rk': 5, 'G?dkrk': 4, 'G?N@x{': 4, 'G?oqx{': 5, 'G?ouX{': 4, 'G?K}Vk': 4, 'GW?X}{': 4, 'G@J@}{': 4, 'G?N@z{': 5, 'G?YSz{': 4, 'G?N@~{': 4, 'G?KtYw': 4, 'G?qipk': 4, 'GP?y]s': 4, 'G?Mirk': 4, 'G?fHrk': 5, 'G?hPx{': 4, 'G?YQx{': 4, 'G?hUX{': 5, 'G?Mivk': 4, 'GP@H}{': 4, 'G?hPz{': 4, 'G?osz{': 4, 'G?hP~{': 4, 'Go?Zzw': 4, 'G?ovvg': 4, 'GW?Z}w': 4, 'GIAJ|w': 4, 'Go?Z~w': 4, 'Go?Zz{': 4, 'G?ovvk': 4, 'GW?Z}{': 4, 'GIAJ|{': 4, 'Go?Z~{': 4, 'G?YRzw': 4, 'G?NDzw': 4, 'G?hTzw': 4, 'G?YR~w': 4, 'G?YRz{': 4, 'G?NDz{': 4, 'G?hTz{': 4, 'G?YR~{': 4, 'G?ov~w': 4, 'G?ov~{': 4, 'G?MJjg': 4, 'GAOxtK': 4, 'G?Xrc{': 4, 'G@X_{{': 4, 'GGOxs{': 5, 'GIHHk{': 4, 'G@TP[{': 4, 'GADjT{': 4, 'GAOxt{': 4, 'G@TP^{': 4, 'GAI[rK': 5, 'GOOxqk': 5, 'GCGiyw': 4, 'G@_iyw': 5, 'G@Y_yk': 4, 'G?dPxw': 5, 'GC`XrK': 4, 'G@C\\ZW': 4, 'G?MqZc': 4, 'GQ?xu[': 4, 'G@Q[r[': 5, 'GOOxq{': 5, 'GG_xq{': 4, 'GHEP][': 4, 'GCTPX{': 5, 'GC`Xr[': 5, 'GCOxp{': 4, 'G@h_y{': 4, 'G?Mre[': 4, 'GG_xu{': 4, 'GAI[r{': 4, 'GCOxr{': 4, 'G@h_}{': 4, 'GCOxv{': 4, 'G@UlQk': 4, 'GAOx|o': 4, 'GAM[rK': 4, 'GAdjTk': 4, 'GBePZ[': 4, 'GDHYr[': 4, 'GE_xr[': 4, 'GAwZLk': 4, 'G@TT\\[': 4, 'G@Xa{{': 4, 'GAKt][': 4, 'G@eQz[': 4, 'GAKuX{': 4, 'G@H\\]s': 4, 'GDHYv[': 4, 'GAXc|{': 4, 'G@eRZ{': 4, 'G@TTZ{': 4, 'GCKuZ{': 4, 'GGSml{': 4, 'G@TT^{': 4, 'G@TjSk': 4, 'GHDYt[': 4, 'GBTP\\[': 4, 'GHKq[{': 4, 'GBSZL[': 4, 'GGKsy{': 4, 'GAKsz[': 4, 'G?[szk': 4, 'GHKq]{': 4, 'GGTP|{': 4, 'GAOzt{': 4, 'GGKq|{': 4, 'GADjt{': 4, 'GGKq~{': 4, 'GAKt]W': 5, 'GASxtK': 4, 'GCSxrK': 5, 'GKCxu[': 4, 'GB_xu[': 5, 'GPKqY{': 5, 'GHKsY{': 4, 'GDCzU[': 4, 'GOKqy{': 4, 'GPKq]{': 4, 'GOKq}{': 4, 'GCKr]{': 4, 'GGKsz{': 4, 'GOKqz{': 4, 'GDCj]{': 4, 'GOKq~{': 4, 'G?\\ilc': 5, 'G?hZtg': 5, 'GIci\\k': 4, 'GAwq\\k': 4, 'GDDZR[': 4, 'GEC|R[': 4, 'GBc\\J[': 4, 'G?trTk': 4, 'GAW\\nK': 4, 'GHOi{{': 4, 'GBG\\][': 4, 'GBDL\\[': 4, 'GIO\\l[': 4, 'GAWZ\\k': 4, 'G@Dl]s': 4, 'G?Lup{': 4, 'G?eqzs': 4, 'G?Lt]s': 4, 'GDDZV[': 4, 'GIHK|{': 4, 'GGLMl{': 4, 'GBDLZ{': 4, 'GDCmZ{': 4, 'GDEJZ{': 4, 'G?\\el{': 4, 'GBDL^{': 4, 'G@LYvK': 4, 'GAO|p{': 4, 'GAKq|[': 5, 'G@HY{{': 4, 'G@TP~[': 4, 'GAOx|{': 4, 'G@HY|{': 4, 'GADj\\{': 4, 'G@HY~{': 4, 'GCSxvK': 4, 'GCKqz[': 4, 'GCKq~[': 4, 'GC`Xz{': 4, 'G@IYz{': 4, 'G@Ej]{': 4, 'G@IY~{': 4, 'GGTT|w': 4, 'G@H\\~o': 4, 'GGKu~w': 4, 'GGTT|{': 4, 'G@H\\~s': 4, 'GGKu~{': 4, 'G@TT~W': 4, 'GAQx~s': 4, 'G@TT~[': 4, 'GAO||{': 4, 'GAOz|{': 4, 'G@H\\}{': 4, 'GAO|~{': 4, 'G@H^rw': 4, 'G@Hy~s': 4, 'G@H^r{': 4, 'G@H\\z{': 4, 'G@HZ~{': 4, 'G@Iy~s': 4, 'G@IZz{': 4, 'G@IZ~{': 4, 'G?Tt~o': 4, 'G@FZ^s': 4, 'G?Tt~s': 4, 'GAO|~[': 4, 'GADj|{': 4, 'G@Dl}{': 4, 'GADl|{': 4, 'G?Lv]{': 4, 'GADl~{': 4, 'G@H^~w': 4, 'G@H^~{': 4, 'G@UdQk': 5, 'GIEJPk': 5, 'GLOic[': 5, 'G@U`Yk': 5, 'G@iaqk': 5, 'G@Sp]K': 5, 'GAWXlK': 5, 'GBP`s[': 5, 'G@DleS': 5, 'GDOhYk': 5, 'GCXPk[': 5, 'G@ohik': 5, 'GPOgyk': 5, 'GGIYrc': 5, 'GAg[jK': 5, 'G@FLbS': 5, 'G?Ysrc': 5, 'G@ogyk': 5, 'GAOxlS': 5, 'GC`XjS': 5, 'GGISyw': 5, 'G@p_w{': 5, 'G@Cr]W': 5, 'G?Yozc': 5, 'G?MMjg': 5, 'GbGJK{': 5, 'GDIaY{': 5, 'GBPcX{': 5, 'GOKuI{': 5, 'GSGqY{': 5, 'GILDK{': 5, 'GH_\\I{': 5, 'G`Oih{': 5, 'GWCsY{': 5, 'GH_ki{': 5, 'GhD@[{': 5, 'GAgqX{': 5, 'GCUJH{': 5, 'G_dHh{': 5, 'GS?zQ{': 5, 'G@DmP{': 5, 'GAgZH{': 5, 'GB@mP{': 5, 'GCoZH{': 5, 'G?MvA{': 5, 'GDAjQ{': 5, 'GBPc\\{': 5, 'G`Oil{': 5, 'GOMIj{': 5, 'GGSkj{': 5, 'G@g]J{': 5, 'GOcij{': 5, 'GB@mT{': 5, 'GGSkn{': 5, 'G_Kta[': 4, 'GIM@i[': 4, 'GBXcc[': 4, 'GGeQh[': 5, 'G_Kpi[': 4, 'GCW[jK': 5, 'GOShik': 5, 'GIQHpk': 4, 'G@G]]W': 4, 'GGHS{w': 5, 'G_Opxw': 5, 'GCX_w{': 4, 'G?Kmmg': 4, 'G?cjjg': 5, 'GBYBK{': 4, 'G`G\\I{': 4, 'GPQPY{': 5, 'GI_qX{': 4, 'GLP@[{': 4, 'GGeQX{': 5, 'G_KqX{': 4, 'Go?xq{': 4, 'G@r?x{': 4, 'GCDjP{': 5, 'G?Yta{': 5, 'G?pr`{': 4, 'GI_q\\{': 4, 'G_KsZ{': 4, 'GAi_z{': 5, 'GCX_z{': 4, 'G?prd{': 4, 'GCX_~{': 4, 'G@h\\Ac': 5, 'G`G[rG': 4, 'GBZD?{': 4, 'GoSr?{': 5, 'GRXCG{': 4, 'GC]@jK': 5, 'G_`pps': 4, 'G`I_ys': 4, 'G@F`uS': 4, 'G?jPrc': 5, 'G?hpuc': 5, 'G?n@jc': 4, 'G@G]mW': 4, 'GGO[|g': 5, 'GW?[yw': 5, 'G?K]nG': 4, 'G?W]lg': 5, 'GDZE@{': 4, 'GYQ?x{': 4, 'GbHCX{': 5, 'GpP?x{': 4, 'GLPCX{': 4, 'GC`rP{': 5, 'G__z`{': 4, 'G?Ne`{': 4, 'G?Yu`{': 5, 'G?qr`{': 4, 'GYa?z{': 4, 'GC`rR{': 4, 'G?Neb{': 5, 'G?ptb{': 4, 'G?Nef{': 4, 'GCDnfO': 4, 'GC`zbS': 4, 'GoDsZs': 4, 'GC\\cZk': 4, 'GGlKjk': 5, 'GCx_zk': 4, 'GWB[rs': 4, 'G_MJjk': 4, 'GAgZnK': 5, 'GB_Z^K': 4, 'GCDnfS': 4, 'G_MHzk': 4, 'G@JH}s': 4, 'GCDh~S': 5, 'GIA\\r[': 5, 'Gg?|q{': 4, 'G@smNk': 4, 'GKb@z{': 4, 'GCYJj{': 4, 'GAhLj{': 5, 'G_LLj{': 4, 'GgA\\r{': 4, 'GCYJn{': 4, 'G?L~Ec': 5, 'G?h\\rg': 5, 'GaKi\\k': 5, 'GG\\Klk': 5, 'GBS\\J[': 5, 'GDK]J[': 5, 'GDcZJ[': 5, 'G?\\mdk': 5, 'GDOZZ[': 5, 'GEG\\Z[': 5, 'GDDLZ[': 5, 'GAEjp{': 5, 'G?Uszs': 5, 'GBS\\N[': 5, 'GaHH|{': 5, 'GAhJl{': 5, 'GECjZ{': 5, 'G@FLr{': 5, 'GCDlr{': 5, 'G?xRl{': 5, 'GECj^{': 5, 'G?X\\tg': 5, 'G?\\jck': 4, 'GILK\\k': 4, 'G_[q\\k': 4, 'GDgYj[': 5, 'GBW[j[': 4, 'G?\\uTk': 4, 'GBEJZ[': 4, 'GBW[n[': 4, 'GIQH|{': 4, 'G_LJl{': 4, 'GDDLZ{': 5, 'GBEJZ{': 4, 'G?^Bl{': 4, 'GBEJ^{': 4, 'G?LvMo': 5, 'G?prlo': 4, 'G?pzdc': 4, 'G?K~Ug': 4, 'G?MzUc': 5, 'G?Mjmo': 5, 'G?MzeS': 4, 'Go`ozs': 4, 'G_bprs': 4, 'G?tlbk': 5, 'G?xsrk': 4, 'G?^Lbk': 4, 'GX?Y}[': 5, 'GBENJ[': 4, 'GFAJZ[': 4, 'G_O~`{': 4, 'G?N`}s': 4, 'G?l`}k': 5, 'G?n@zk': 4, 'G?nJfk': 4, 'Gs@Hz{': 4, 'Go@\\r{': 4, 'G?xTj{': 5, 'G?^Dj{': 4, 'G?yRj{': 4, 'G?yRn{': 4, 'G@pg~c': 5, 'GALL\\k': 5, 'GGOzs{': 5, 'G@H\\u[': 5, 'GADlt[': 5, 'GGO~c{': 5, 'GCYHzk': 5, 'GGQZp{': 5, 'G@JLq{': 5, 'GCDjt[': 5, 'GGQ^`{': 5, 'GAQhx{': 5, 'G@JKy{': 5, 'G@W]^k': 5, 'G@oZ^k': 5, 'GO_yz{': 5, 'G@FJZ{': 5, 'G@EmZ{': 5, 'GOIYz{': 5, 'GB@m\\{': 5, 'G@FJ^{': 5, 'GCXg~c': 4, 'GCDlr[': 5, 'GCWZZk': 4, 'GGI[y{': 5, 'G_Oxx{': 4, 'G__xzk': 4, 'G@FMX{': 4, 'GCWZ^k': 4, 'G__xz{': 4, 'GAElZ{': 5, 'GCDjZ{': 4, 'G?prl{': 4, 'GCDj^{': 4, 'G?Neno': 4, 'Go?zq{': 4, 'GIAZt[': 5, 'GgAZp{': 4, 'Gg?zs{': 4, 'GAO|l[': 5, 'G?K~Mk': 4, 'Go@X~s': 4, 'GC`rZ{': 4, 'G?Nej{': 5, 'G?ptj{': 4, 'G?Nen{': 4, 'GEKX^K': 4, 'G@G}]s': 4, 'G?K}rk': 5, 'G?eZrk': 4, 'G?K~Uk': 4, 'GEChz[': 5, 'G?dszs': 4, 'G@DmX{': 5, 'G?NPx{': 4, 'G@K]n[': 4, 'GECh~[': 4, 'G@JH}{': 4, 'G?NPz{': 5, 'G?dsz{': 4, 'G?N`}{': 4, 'G?NP~{': 4, 'GB_^^W': 4, 'GBEJ~W': 4, 'GECn^w': 4, 'GB_^^[': 4, 'GBEJ~[': 4, 'GECn^{': 4, 'G@FN^o': 4, 'G_Qx~s': 4, 'G@FN^s': 4, 'G__zz{': 4, 'GGI]z{': 5, 'G_Oz|{': 4, 'G_O|~k': 4, 'G__z~{': 4, 'GAEj~o': 5, 'GAD|^s': 5, 'GAEj~s': 5, 'GAEjz{': 5, 'G@FLz{': 5, 'GCDlz{': 5, 'GAEj~{': 5, 'GCDz^s': 4, 'GCDjz{': 4, 'GCDj~{': 4, 'G?dv^o': 4, 'G?fjns': 4, 'G?dv^s': 4, 'G?UvZ{': 5, 'G?dvZ{': 4, 'G?qrz{': 4, 'G?qr~{': 4, 'GCDn~w': 4, 'GCDn~{': 4, 'G@OxuK': 4, 'GCGxq[': 5, 'G@KsY[': 4, 'G?KzeK': 5, 'G?K{Zc': 4, 'GAGxu[': 5, 'GOCxq{': 4, 'GBGg}[': 4, 'G@Kq][': 4, 'GCGxq{': 5, 'G@Kim[': 5, 'G?K|a{': 4, 'G?Kze[': 4, 'GGCxu{': 4, 'GAGxu{': 5, 'G@KsZ{': 4, 'G?Kze{': 4, 'G@Kq^{': 4, 'GEGhW{': 4, 'GDPHW{': 5, 'G?]SjK': 4, 'G?K~Ec': 4, 'G@Kg}K': 4, 'G@CzMS': 5, 'G?K}Mc': 5, 'G?FXps': 4, 'G?Kx]c': 4, 'G?HY|o': 5, 'GWCo}[': 4, 'GWGWy{': 5, 'GBaGz[': 4, 'GF?h][': 4, 'G@KuM[': 4, 'G@ohi{': 5, 'GCW[j[': 5, 'G@F`u[': 4, 'G?sph{': 4, 'GAS\\H{': 5, 'G?wpi{': 5, 'G?]Sj[': 4, 'GWGW}{': 4, 'G@ohm{': 4, 'G?spj{': 5, 'G?]Sj{': 4, 'G?wpm{': 4, 'G?spn{': 4, 'GAopxw': 5, 'G@KxuK': 4, 'GEGxu[': 4, 'GWCxq{': 4, 'GFCh][': 4, 'G@Ku][': 4, 'G@Kq}[': 5, 'G@Kp}[': 4, 'GWCxu{': 4, 'G@Ku]{': 4, 'G@KuZ{': 4, 'G@K^M{': 4, 'G@Ku^{': 4, 'GBGxu[': 4, 'G@IXzs': 4, 'G@IYx{': 4, 'G?K|rk': 4, 'GGKp}{': 4, 'G@HX}{': 4, 'G@Kr]{': 4, 'G@G{z{': 4, 'G?Lp}{': 4, 'G@Gy~{': 4, 'G@Gx}{': 4, 'G?Kx}{': 4, 'G?Kx~{': 4, 'G?K~vg': 4, 'G?Np~s': 4, 'G@G}}{': 4, 'G?K~vk': 4, 'G@Gz}{': 4, 'G@G}~{': 4, 'G?[x~k': 4, 'G?K|z{': 4, 'G?Kz~{': 4, 'G?sx~k': 4, 'G?K}~k': 4, 'G?K}z{': 4, 'G?K}}{': 4, 'G?K~]{': 4, 'G?K}~{': 4, 'G?K~~w': 4, 'G?K~~{': 4, 'GJO_{[': 5, 'G?W{jc': 4, 'G?Mbiw': 5, 'G?`Xzo': 5, 'GAWrK{': 4, 'GHHG{{': 4, 'GIOp[{': 4, 'GIGZK{': 4, 'GGGys{': 5, 'G@Wik{': 4, 'GGHZc{': 5, 'G?Szc{': 4, 'G?Wzc{': 5, 'GIGY\\{': 4, 'GALa\\{': 4, 'G?Szd{': 4, 'G?\\al{': 4, 'G?Szf{': 4, 'GDGgy[': 5, 'GBOkW{': 5, 'G?]`ik': 5, 'G@Wkik': 5, 'G@cZJK': 5, 'GAK]LK': 5, 'G@DtUS': 5, 'G?Ypqk': 5, 'G?czJc': 5, 'G?M]bK': 5, 'G@G\\Yw': 5, 'G?MrIs': 5, 'G?MZJc': 5, 'G?M]Jc': 5, 'G?EXzo': 5, 'G?C|Zo': 5, 'G?PX|o': 5, 'G?Pxss': 5, 'GQCp][': 5, 'GCKrM[': 5, 'GPHGy{': 5, 'GHIGy{': 5, 'GDQGz[': 5, 'GBE`][': 5, 'GPCq][': 5, 'GGG{q{': 5, 'GOGyq{': 5, 'G@o[j[': 5, 'GD?zU[': 5, 'G@Wki{': 5, 'G@gii{': 5, 'GChOz[': 5, 'G@ErU[': 5, 'G?cz`{': 5, 'GEDHX{': 5, 'G?W|a{': 5, 'GAcZH{': 5, 'G?gza{': 5, 'G?NSr[': 5, 'GPHG}{': 5, 'GOGyu{': 5, 'G@gim{': 5, 'G?Upr{': 5, 'GCCzR{': 5, 'G?NSr{': 5, 'G?gze{': 5, 'G?czf{': 5, 'G@\\acK': 5, 'GKXPc[': 5, 'G?hsrc': 5, 'G?wpik': 5, 'G?krIk': 5, 'G?yQhk': 5, 'G?lSjK': 5, 'G?iZbc': 5, 'G?Wxmc': 5, 'G@CjmW': 5, 'G?Ypis': 5, 'G?UXnC': 5, 'G?qXjc': 5, 'G?MUjW': 5, 'G?wYhk': 5, 'G?XW|c': 5, 'G?FLZo': 5, 'GbO`[{': 5, 'GaOpX{': 5, 'GX?[Y{': 5, 'GHISY{': 5, 'GJOc[{': 5, 'GGPsp{': 5, 'GP?}Q{': 5, 'G@IuQ{': 5, 'GOIqq{': 5, 'G?Lm`{': 5, 'G?lah{': 5, 'G?d^@{': 5, 'G?fJ`{': 5, 'GaOp\\{': 5, 'GGPst{': 5, 'G?X\\b{': 5, 'G?g}b{': 5, 'G?iZb{': 5, 'G?X\\f{': 5, 'G?L^N_': 5, 'G?XX~_': 4, 'GAla\\k': 4, 'GFDHZ[': 4, 'GFEHZ[': 4, 'G?|alk': 4, 'GAK^NK': 4, 'GAXH|k': 4, 'GB?~U[': 5, 'G?Sz^c': 4, 'GFDH^[': 4, 'GAXLl{': 4, 'GAK^J{': 4, 'GCK^J{': 4, 'G?X^d{': 4, 'GAK^N{': 4, 'GALJ\\k': 4, 'GA[XnK': 4, 'GADlp{': 4, 'G?[q|k': 4, 'G?\\R\\k': 4, 'G?XZtk': 5, 'GBDH~[': 4, 'GAOz\\{': 4, 'G@SZn[': 4, 'G?Szl{': 4, 'G?LZl{': 4, 'G?Tr\\{': 4, 'G?LZn{': 4, 'G@kYnK': 5, 'GCDjp{': 5, 'GAK\\^K': 5, 'GAEjX{': 5, 'GCDjX{': 5, 'G@EmY{': 5, 'GACzt[': 5, 'G?d\\rk': 5, 'G?Lluk': 5, 'GADX|[': 5, 'GDDH~[': 5, 'GOGy}{': 5, 'G@cZn[': 5, 'G?Upz{': 5, 'GCCzZ{': 5, 'G?NSz{': 5, 'G?Yp}{': 5, 'G?czn{': 5, 'GC[XnK': 4, 'G?kqzk': 4, 'G@Hk}s': 4, 'G@EjY{': 4, 'G@Dj[{': 4, 'GAC|r[': 4, 'G?dZtk': 4, 'GCCzr[': 5, 'G?Llms': 5, 'GDCi~[': 4, 'G@Ii}{': 4, 'GCKZn[': 4, 'G?L\\j{': 4, 'G?d\\j{': 4, 'G?MZj{': 4, 'G?Mjm{': 4, 'G?MZn{': 4, 'G?xXnc': 5, 'G?Yrq{': 5, 'G?jPzs': 5, 'G?NTr[': 5, 'G?dtZs': 5, 'GGHZk{': 5, 'G?W|mk': 5, 'G@Er][': 5, 'G?Utj[': 5, 'G?X\\tk': 5, 'G?N`y{': 5, 'G?wq~k': 5, 'GGPs|{': 5, 'G?W}vk': 5, 'G?Naz{': 5, 'G?g}j{': 5, 'G?Mmj{': 5, 'G?ejj{': 5, 'G?Na~{': 5, 'G?S~`{': 4, 'G?Ky~c': 4, 'G?L\\h{': 4, 'G?cxzk': 5, 'G@DY|[': 4, 'G?V`x{': 5, 'G?dXx{': 4, 'G?hYx{': 5, 'G@DX~[': 4, 'GACx~[': 4, 'G?cxz{': 4, 'G?TX|{': 4, 'G?Wx}{': 4, 'G?Sx~{': 4, 'G?UrX{': 5, 'G?MrY{': 4, 'G?Li~k': 4, 'G?Li|{': 4, 'G?XX~{': 4, 'G?dX~c': 4, 'G?dqx{': 5, 'G?LZk{': 4, 'G?Ncy{': 5, 'G?XX{{': 5, 'G@EY~[': 4, 'G?S{z{': 4, 'G?dX~[': 4, 'G?dX~{': 4, 'G?S~vg': 4, 'G?Vp~s': 4, 'GAC~^[': 4, 'G?S~vk': 4, 'GACz~[': 4, 'G?S~n[': 4, 'GAC~^{': 4, 'G?\\X~k': 4, 'G?XZ|{': 4, 'G?Sz~{': 4, 'G?]X~k': 4, 'G?S|~k': 4, 'G@D\\~[': 4, 'G?S|z{': 4, 'G?czz{': 4, 'G?S}|{': 4, 'G?Ll}{': 4, 'G?cz~{': 4, 'G?li~k': 4, 'G?X\\|{': 4, 'G?X\\~{': 4, 'G?S~~w': 4, 'G?S~~{': 4, 'GIKqSK': 4, 'GDXac[': 4, 'GBDbS[': 4, 'G?LteS': 4, 'G?iqrc': 5, 'G?[pmK': 4, 'G?YZbc': 4, 'G?NLbc': 4, 'G?h\\bc': 5, 'G?oxjc': 5, 'G?crjW': 5, 'G?h[jc': 5, 'G?KumW': 4, 'G?KrmW': 4, 'G?Uhjc': 5, 'G?LTmW': 5, 'G?Y[jc': 4, 'G?gYzg': 5, 'G?Xo{s': 4, 'G?`kzo': 4, 'GRP@[{': 4, 'GBXDK{': 4, 'GIOsX{': 4, 'GPG]I{': 4, 'GPIQY{': 5, 'GYO_{{': 4, 'G_Oz`{': 4, 'GW?{q{': 4, 'GGI\\a{': 5, 'GI?}P{': 4, 'G@I^A{': 4, 'GPAZQ{': 5, 'G?LuP{': 4, 'G?dj`{': 5, 'G?uRH{': 5, 'G?v@h{': 4, 'GIOs\\{': 4, 'G_Ozd{': 4, 'GI?}T{': 4, 'G?\\cj{': 4, 'G?kuJ{': 4, 'G?maj{': 5, 'G?\\cn{': 4, 'G?o~f_': 4, 'G?dr^_': 4, 'G?Lu^_': 4, 'G?K}^_': 4, 'G?Mi~_': 5, 'Go@{rs': 4, 'G?|cjk': 4, 'G?o~fc': 4, 'GW?}q{': 4, 'GBA^R[': 4, 'G?NH~c': 4, 'G?hX~c': 5, 'G?~@nk': 4, 'GoAZr{': 4, 'G?Y^b{': 4, 'G?o~f{': 4, 'G?\\knc': 4, 'G?]RZk': 4, 'G?UtZs': 5, 'G?drj[': 4, 'G?o|jk': 4, 'G?Url[': 5, 'G?YZrk': 4, 'G?NLrk': 4, 'G?h\\rk': 5, 'G?NUX{': 4, 'G?]R^k': 4, 'G_Ozl{': 4, 'G?YZvk': 4, 'G?drZ{': 4, 'G?qpz{': 4, 'G?UtZ{': 5, 'G?dr^{': 4, 'GI?|u[': 4, 'G?^Hnc': 4, 'G?erZs': 5, 'G?Xrs{': 4, 'G?Ltu[': 4, 'G?Xrk{': 4, 'G?Mrm[': 4, 'G?hZtk': 5, 'G?[u^k': 4, 'GI?}\\{': 4, 'G?ozvk': 4, 'G?iqz{': 5, 'G?LuZ{': 4, 'G?MuZ{': 4, 'G?Lu^{': 4, 'G?K}^c': 4, 'G?Lp}[': 4, 'G?ppx{': 4, 'G?Xs{{': 4, 'G?Kx}[': 4, 'G?NMX{': 4, 'G?K}^k': 4, 'G?ox~k': 4, 'G?K}Z{': 4, 'G?Y[z{': 4, 'G?K}^{': 4, 'G?L\\^c': 5, 'G?LtY{': 5, 'G?NSz[': 5, 'G?drX{': 5, 'G?Yq{{': 5, 'G?TtX{': 5, 'G?MuY{': 5, 'G?K|Y{': 5, 'G?h]X{': 5, 'G?Mi~k': 5, 'G?Uh~k': 5, 'G?gyz{': 5, 'G?h[z{': 5, 'G?Mi~{': 5, 'G?o~vg': 4, 'G?rp~s': 4, 'G?o~nk': 4, 'G?o~vk': 4, 'G?o~j{': 4, 'G?Y^j{': 4, 'G?o~n{': 4, 'G?\\k~k': 4, 'G?YZz{': 4, 'G?NLz{': 4, 'G?h\\z{': 5, 'G?YZ~{': 4, 'G?o~~w': 4, 'G?o~~{': 4, 'GBY[vK': 4, 'GBeRZ[': 4, 'GAQzts': 4, 'GAO||w': 4, 'GC`jzw': 4, 'G@J]p{': 4, 'G@FnQ{': 4, 'G?NNng': 4, 'GBeR^[': 4, 'GC`zr{': 4, 'G@J]r{': 4, 'GCFnR{': 4, 'G@J]v{': 4, 'G@J^vo': 4, 'G@J]~o': 4, 'G@J}vs': 4, 'G@J^vs': 4, 'G@J^v{': 4, 'GC`~r{': 4, 'GC`zz{': 4, 'G@J]~{': 4, 'G@J^~{': 4, 'GMGxu[': 4, 'G@JZrs': 4, 'G@J\\rs': 4, 'G@H}us': 4, 'G@H|us': 4, 'GAPx|s': 4, 'G@J[zs': 4, 'G@FmZs': 5, 'G@Gz}w': 4, 'GADx~S': 4, 'G?M^jw': 4, 'G?Nru[': 4, 'GWKq}{': 4, 'GHKu]{': 4, 'GAP|t{': 4, 'G@H}r{': 4, 'G@I}r{': 4, 'GAD~T{': 4, 'G@H}v{': 4, 'G?\\p~c': 4, 'G@Hzus': 4, 'G?Mrzw': 4, 'GADzt[': 5, 'GHGy}{': 4, 'G@Hzu{': 4, 'G?Lzt{': 4, 'G?Tzt{': 4, 'G?Lzv{': 4, 'G?kzjk': 4, 'G?]pzk': 4, 'G?Mzjs': 4, 'G?NTzw': 5, 'G?K|zw': 4, 'GPGy}{': 4, 'G@Izu{': 4, 'G?kzj{': 4, 'G?Mzu{': 4, 'G?Mzv{': 4, 'GBEi~S': 4, 'GAEzvS': 4, 'G?lri{': 4, 'G?s|jk': 4, 'G?]\\jk': 4, 'G?nbi{': 4, 'G?T|vc': 4, 'GBDZ\\[': 4, 'G?^Th{': 4, 'G?\\\\lk': 4, 'G?^eh{': 4, 'GADz\\s': 4, 'G?N\\js': 4, 'G?Utzw': 5, 'G?Nb}w': 5, 'G?sxzk': 4, 'G?Uxzs': 4, 'G?\\i|k': 4, 'G?S}|w': 4, 'G?h\\zw': 5, 'GDDZ^[': 4, 'GBD\\^[': 4, 'GAD|v[': 4, 'G?\\\\j{': 4, 'G?k}j{': 4, 'G?mZj{': 4, 'G?\\ml{': 4, 'G?\\\\n{': 4, 'G?L~no': 4, 'G?{znk': 4, 'G?[~nk': 4, 'G@H~u{': 4, 'G?L|~s': 4, 'G?[~n{': 4, 'G@J^r{': 4, 'G@H}}{': 4, 'G@H}~{': 4, 'G?L~r{': 4, 'G@Hz}{': 4, 'G?Mzz{': 4, 'G?Lz~{': 4, 'G@Iz}{': 4, 'G?Mz~{': 4, 'G?L~~{': 4, 'GEwXnK': 4, 'G@J^Us': 4, 'GAFjts': 4, 'G?frrs': 4, 'G?NvUs': 4, 'G@F^VS': 4, 'G?d~Vc': 4, 'G@Fj]s': 4, 'GCFjZs': 4, 'G?Nfmw': 4, 'G?N^`{': 4, 'G?S|~g': 4, 'G?Nr]s': 4, 'G?frZs': 4, 'GFEJ^[': 4, 'GBc^N[': 4, 'GC`~R{': 4, 'G?N^b{': 4, 'G?d~b{': 4, 'G?fvR{': 4, 'G?N^f{': 4, 'G?\\s~c': 4, 'GBEZ^S': 4, 'G?\\rk{': 4, 'G?Tt|w': 4, 'G?drzw': 4, 'G?fbzw': 4, 'G?K}}w': 4, 'G?czzw': 4, 'G?X\\|w': 4, 'G?Xzs{': 4, 'GBDk~[': 4, 'GCDzv[': 4, 'G?mqz{': 4, 'G?\\sz{': 4, 'G?\\u\\{': 4, 'G?\\s~{': 4, 'G?lu^c': 4, 'G?lrm[': 4, 'G?^bk{': 4, 'G?Lv]w': 4, 'G?dvZw': 4, 'G?K~]w': 4, 'G?Mz]s': 4, 'G?Mzu[': 4, 'G?^c~k': 4, 'G?Nmvk': 4, 'G?Nmr{': 4, 'G?^Lj{': 4, 'G?Nmv{': 4, 'G?N^no': 4, 'G?}Znk': 4, 'G?s~nk': 4, 'GCD~v[': 4, 'G?d~^s': 4, 'G?s~n{': 4, 'GCFnr{': 4, 'G@Fn]{': 4, 'G?N^n{': 4, 'G?L}~s': 4, 'G?Uz~s': 4, 'G?L}~k': 4, 'G?NZz{': 4, 'G?N\\z{': 4, 'G?NZ~{': 4, 'G?]Z~k': 4, 'G?dz~k': 4, 'G?U|z{': 4, 'G?dzz{': 4, 'G?fjz{': 4, 'G?dz~{': 4, 'G?Nv]{': 4, 'G?L~]{': 4, 'G?Nm~{': 4, 'G?d~~{': 4, 'G?N~vs': 4, 'G?Nv~w': 4, 'G?L~~w': 4, 'G?N^~w': 4, 'G?N~v{': 4, 'G?N~~{': 4, 'G?\\rc[': 3, 'GBDjS[': 4, 'G?\\rc{': 4, 'GHTP[{': 4, 'G?\\rd{': 4, 'GBX_~{': 3, 'GB`jSk': 4, 'GKGiyw': 4, 'GQKsY[': 5, 'GOTPxw': 4, 'GDPjO{': 5, 'GBElQ[': 4, 'G?xrck': 4, 'GIKs[[': 4, 'GKDHxw': 5, 'GHTH[k': 4, 'GBEkZS': 5, 'G?\\uLc': 4, 'G?Ezro': 4, 'G?\\q\\c': 4, 'G?Q|ro': 4, 'G`X_{{': 4, 'GaOxp{': 4, 'GK_xq{': 4, 'GWHYs{': 4, 'GBXc[{': 4, 'GKTPX{': 4, 'GSKqY{': 5, 'GHoik{': 4, 'G?lr`{': 4, 'G?tr`{': 4, 'GDgZI{': 4, 'G?xrc{': 4, 'GaOxt{': 4, 'GKTP\\{': 4, 'G?lrb{': 4, 'GSKqZ{': 4, 'G?trd{': 4, 'G?lrf{': 4, 'GBXc{w': 4, 'G@`zro': 4, 'G@Hzuo': 4, 'GO\\rc{': 4, 'G_\\r`{': 4, 'GXHYs{': 4, 'GBXc{{': 3, 'GBX`{{': 4, 'G_\\rd{': 3, 'GBXc|{': 4, 'GBXcz{': 3, 'GIKu\\{': 4, 'GBXc~{': 3, 'GG\\rc{': 3, 'GBXa|{': 4, 'GIOx|{': 3, 'G?\\rl{': 4, 'G?\\rn{': 3, 'G?\\vvg': 4, 'GIQx~s': 3, 'GIO||{': 3, 'G?\\vvk': 3, 'GIOz|{': 3, 'GIO|~{': 3, 'G?lrzw': 4, 'G?\\zvk': 3, 'G?\\r~{': 3, 'G?]|rk': 4, 'G?lzvk': 4, 'GHH\\}{': 4, 'G?\\tz{': 4, 'G?\\t|{': 4, 'G?\\u|{': 4, 'G?\\t~{': 4, 'G?\\v~w': 3, 'G?\\v~{': 3, 'GsXP_[': 4, 'GqG[rK': 4, 'G?lvEc': 4, 'GEG\\ZW': 5, 'GBG\\]W': 4, 'G?xqlc': 5, 'G?[vMg': 4, 'G?F\\ro': 4, 'G?Izuo': 3, 'GQouH{': 4, 'GgLKh{': 4, 'GIQkp{': 4, 'Gc`rP{': 4, 'G?ur`{': 4, 'G?^e`{': 4, 'GSXSZ{': 4, 'G?^Tb{': 4, 'G?zTb{': 4, 'G?urf{': 4, 'G`Xc{w': 4, 'GHTS|W': 4, 'G@Izuo': 4, 'G?Nmv_': 4, 'GRQ[r[': 4, 'G[KqY{': 4, 'GFFLR[': 4, 'GQKu][': 4, 'GQKq}[': 4, 'GIQX|s': 4, 'G?lp~c': 4, 'GXIYu{': 4, 'GQeRZ{': 4, 'GQKuZ{': 4, 'GEg^J{': 4, 'GQKu^{': 4, 'GJKs][': 4, 'G?ltrk': 5, 'GPHYy{': 4, 'GHI[y{': 4, 'GDFJZ[': 4, 'GKKr]{': 4, 'GaOx|{': 4, 'G?lrj{': 4, 'G?]tj{': 4, 'G?trl{': 4, 'G?lrn{': 4, 'GHTS|[': 4, 'GRKq][': 4, 'G?mrrk': 4, 'G?\\trk': 4, 'G?\\utk': 4, 'GHHY{{': 4, 'G?]trk': 4, 'GPHZq{': 4, 'GIKt]{': 4, 'GIQX|{': 4, 'GQKr]{': 4, 'GPIYz{': 4, 'G?]rj{': 4, 'G?^Rl{': 4, 'G?]rn{': 4, 'G?z\\bc': 4, 'GBEm^S': 4, 'GEkZNK': 4, 'G?urrk': 4, 'GBFJt[': 4, 'G?^Rls': 4, 'G?lvUk': 4, 'GBDm\\[': 4, 'G?^elk': 4, 'GDoZn[': 4, 'GS`iz{': 4, 'G?ttj{': 4, 'G?^Tj{': 4, 'G?nej{': 4, 'G?^Tn{': 4, 'G?lvvg': 4, 'GPJY~s': 4, 'GaO||{': 4, 'G?lvvk': 4, 'GPHZ}{': 4, 'GHIZ}{': 4, 'GPH]~{': 4, 'G?mzrk': 4, 'G?]zvk': 4, 'G?lrz{': 4, 'G?ltz{': 4, 'G?lr~{': 4, 'G?\\}tk': 4, 'G?\\u|w': 4, 'G?nmrk': 4, 'G?^\\vk': 4, 'GDDn]{': 4, 'G?^R|{': 4, 'G?urz{': 4, 'G?lv]{': 4, 'G?ur~{': 4, 'G?lv~w': 4, 'G?lv~{': 4, 'GImta[': 3, 'Go\\rc{': 3, 'GIQ|ts': 3, 'GIO||w': 3, 'GHI]}w': 4, 'G?[~ng': 4, 'G?]^ng': 4, 'GbXc|{': 3, 'GS`zr{': 3, 'G?^vb{': 3, 'G?nvb{': 4, 'G?^vf{': 3, 'G?^vno': 3, 'G?\\~vg': 3, 'G?l~vg': 4, 'G?|~fk': 3, 'GiO||{': 3, 'GIQ~t{': 3, 'G?|vn{': 3, 'GIQ||{': 3, 'G?^vn{': 3, 'G?^v~{': 3, 'GIQzts': 4, 'G?|rjk': 3, 'G?}rjk': 4, 'G?\\~fc': 3, 'GIPx|s': 4, 'G?]vjw': 4, 'G?Lz~o': 4, 'G?\\{~c': 4, 'GiOx|{': 3, 'GIP|t{': 4, 'G?\\~b{': 3, 'G?\\~d{': 4, 'G?\\~f{': 3, 'G?^r~s': 3, 'G?\\~nk': 3, 'G?\\~vk': 3, 'G?^r~{': 3, 'G?^rz{': 3, 'G?lzz{': 4, 'G?\\z~{': 3, 'G?nrz{': 4, 'G?^tz{': 4, 'G?mzz{': 4, 'G?lz~{': 4, 'G?\\~~{': 3, 'G?nrvc': 4, 'G?~Tjk': 4, 'G?l~fc': 4, 'G?lznc': 4, 'G?]znc': 4, 'G?nZnc': 4, 'G?Mz~o': 4, 'G?L}~o': 4, 'G?Nm~o': 4, 'GXIY}{': 4, 'GHI}u{': 4, 'G?l~b{': 4, 'G?~Tj{': 4, 'G?l~f{': 4, 'G?^t~s': 4, 'G?]~nk': 4, 'G?l~vk': 4, 'G?^t~{': 4, 'G?^u|{': 4, 'G?\\}|{': 4, 'G?z\\z{': 4, 'G?uz~{': 4, 'G?l~~{': 4, 'G?~vj{': 3, 'G?^v~w': 3, 'G?\\~~w': 3, 'G?l~~w': 4, 'G?^~v{': 3, 'G?^~~{': 3, 'GFzf?{': 2, 'G?~vfc': 3, 'G?|vng': 3, 'G?N~vo': 4, 'Gs`zr{': 3, 'G?~vb{': 3, 'G?~vf{': 2, 'G?~~fc': 2, 'G?~vvk': 3, 'G?~vnk': 2, 'G?~vn{': 2, 'G?~~vk': 2, 'G?~v~{': 2, 'G?~~~{': 2, 'GCO`G{': 5, 'GGEB?{': 5, 'G@`AH{': 5, 'G`?M@{': 4, 'GQ?GX{': 5, 'GGECJ{': 4, 'GK?GZ{': 4, 'G`?G^{': 3, 'G?AYpo': 5, 'G@GSYW': 5, 'GQ?MPg': 5, 'G?dP`[': 5, 'G_Ogpk': 5, 'GAOkPk': 5, 'GQB?Xs': 5, 'GCO_w{': 5, 'G@`@W{': 5, 'G`?JG{': 6, 'GGEAh[': 5, 'GQ?MPk': 5, 'G?Ssb[': 5, 'GC`HRk': 5, 'GCO_x{': 5, 'G_GQX{': 5, 'GAIAX{': 5, 'GQ?MH{': 5, 'G?dPf[': 5, 'GAI?z{': 5, 'GCOcZ{': 5, 'GCO_~{': 5, 'GCGgqK': 6, 'G`?N?w': 5, 'GGC[`[': 5, 'GCOiPk': 6, 'GKOGXk': 5, 'G@PKPk': 5, 'G`OGXk': 5, 'G@bAHs': 5, 'G`B?Xs': 4, 'GCH@W{': 6, 'GQ?HW{': 5, 'GK?JG{': 5, 'GGEBG{': 4, 'G`?N?{': 4, 'GOCYb[': 5, 'GGC[b[': 4, 'G@`KRk': 5, 'GK_GZk': 4, 'GGE?x{': 5, 'GCHAX{': 6, 'GK?IX{': 5, 'G@QAX{': 5, 'G`?IX{': 4, 'G@`EH{': 5, 'G`?MH{': 4, 'GGC[f[': 4, 'GOD?z{': 5, 'GGE?z{': 4, 'GGECZ{': 5, 'GK?KZ{': 4, 'GGE?~{': 4, 'G@`@xw': 5, 'GAIAxw': 5, 'GODAxw': 5, 'GGEAxw': 5, 'G@`DYw': 5, 'G@`@}W': 5, 'G`?LYw': 5, 'G@`@zw': 5, 'GAICzw': 5, 'GQ?Kzw': 5, 'G@`@x{': 5, 'GAIAx{': 5, 'GODAx{': 5, 'GGEAx{': 5, 'G@`DY{': 5, 'G@`@}[': 5, 'G`?LY{': 5, 'G@`@~w': 5, 'G@`@z{': 5, 'GAICz{': 5, 'GQ?Kz{': 5, 'G@`@~{': 5, 'G`?MXw': 4, 'G`?Hzw': 4, 'GGECzw': 4, 'G`?MX{': 3, 'G`?H~w': 3, 'G`?Hz{': 4, 'GGECz{': 4, 'G`?H~{': 3, 'GGEBzw': 4, 'G@`Dzw': 5, 'G`?Lzw': 4, 'GGEB~w': 4, 'GGEBz{': 4, 'G@`Dz{': 5, 'G`?Lz{': 4, 'GGEB~{': 4, 'G`?N~w': 3, 'G`?N~{': 3, 'G@`a_[': 5, 'GB`@G[': 6, 'GCOj?{': 5, 'GGFD?{': 4, 'GWEAG{': 5, 'GK@HO{': 5, 'G@`M@{': 4, 'GODQP{': 5, 'G`AIP{': 4, 'GGESR{': 4, 'G`GOZ{': 5, 'G`GO^{': 4, 'G@LQSK': 5, 'GAGYtK': 5, 'G@O]TK': 5, 'G@O\\UK': 5, 'G?lSbK': 5, 'G@IHis': 5, 'GAQHpk': 5, 'GOCiqk': 5, 'GBg_i[': 5, 'G@PPs[': 5, 'GGCqs[': 5, 'GPGYa[': 5, 'G@aaYs': 5, 'G@dKbK': 5, 'GQcOZK': 5, 'GCGWzK': 5, 'GGEaW{': 6, 'GGEQX[': 5, 'G@`PXs': 5, 'GAM@i[': 5, 'GODQp[': 5, 'GGEIpk': 5, 'G@QLQk': 5, 'G?UTb[': 5, 'GDGJI{': 5, 'GBGLI{': 5, 'GCU@j[': 5, 'GcCHj[': 5, 'GDGZE[': 5, 'GA_ZH{': 5, 'GAJ?x{': 5, 'G_EaX{': 5, 'GCPcX{': 5, 'GDQ?z[': 5, 'G@_ih{': 5, 'GCPPX{': 5, 'G_DPX{': 5, 'GHE@Y{': 5, 'GAIQX{': 5, 'GGDSX{': 5, 'GPD@Y{': 5, 'GOR?x{': 5, 'GAccj[': 5, 'GQCKj[': 5, 'GDGJM{': 5, 'GA_\\J{': 5, 'GOCqZ{': 5, 'G@Q_z{': 5, 'G@`Kj{': 5, 'GODSZ{': 5, 'GPD@]{': 5, 'G@_in{': 5, 'G?C|bO': 5, 'G@`LQk': 5, 'GQ?Yp[': 5, 'GOdOrK': 5, 'G@gqa[': 5, 'GAMAh[': 5, 'GCdPRK': 5, 'G@`PY[': 5, 'GK?Wx[': 5, 'GK@HW{': 5, 'GODaW{': 6, 'GAG]LK': 5, 'GCOXh[': 5, 'GOSSj[': 5, 'GDH@Y{': 5, 'GCScj[': 5, 'GBI@Y{': 5, 'GSOOz[': 5, 'G@Mae[': 5, 'GG`Ox{': 5, 'GOFAX{': 5, 'G_HOx{': 5, 'GQAIX{': 5, 'GCHQX{': 5, 'GCOpX{': 5, 'GDH@]{': 5, 'GQ?[Z{': 5, 'GOOoz{': 5, 'GAISZ{': 5, 'GCOp^{': 5, 'GGc[bK': 4, 'G`GXa[': 5, 'GKcOZK': 5, 'GODQX[': 5, 'GGC]LK': 4, 'GGcSj[': 4, 'G`C`Y{': 5, 'GKCKj[': 4, 'GKE?z[': 4, 'G`GXe[': 4, 'GOOYh{': 5, 'G@RCX{': 4, 'G`AIX{': 4, 'GODQX{': 5, 'G`C`]{': 4, 'GG_[j{': 4, 'G_CpZ{': 5, 'GGESZ{': 4, 'G_Cp^{': 4, 'GAWXcK': 5, 'GOSY`K': 5, 'GIGWsK': 5, 'G@PLSg': 5, 'G@O\\UG': 5, 'G`IIOk': 5, 'GAKZCK': 5, 'G@`H]_': 5, 'G@hR?{': 5, 'GAf@`[': 5, 'GcDH`[': 5, 'GIEK`[': 5, 'G_dP`[': 5, 'GLGIG{': 5, 'GgCpO{': 5, 'GE`H`[': 5, 'GMCKH[': 5, 'GAY?xk': 5, 'GGU?xk': 5, 'GQD?x[': 5, 'GII?w{': 5, 'G@`cYs': 5, 'G@b@Ys': 5, 'GQ@KXs': 5, 'G`GSY[': 5, 'GAM?zK': 5, 'GQCGzK': 5, 'G@`H]c': 5, 'G@ebA{': 5, 'G@XU@{': 5, 'GPEJA{': 5, 'GoCpQ{': 5, 'GH`?x{': 5, 'GE_aX{': 5, 'GcCaX{': 5, 'GKEAX{': 5, 'GcO_x{': 5, 'GBIAX{': 5, 'G`GQX{': 5, 'GCSeH{': 5, 'GKCMH{': 5, 'G@XUD{': 5, 'GP`?z{': 5, 'GII?z{': 5, 'GPDCZ{': 5, 'G`GSZ{': 5, 'GII?~{': 5, 'GALPSK': 5, 'G?K|Ac': 5, 'G@PLSk': 5, 'GGCYtK': 5, 'GOsOjK': 4, 'G@Oqs[': 5, 'G@MAi[': 5, 'G@Os]S': 5, 'G@dSRK': 5, 'G@M@i[': 5, 'GDGia[': 5, 'GBGka[': 4, 'GGCW|K': 4, 'G@QIpk': 5, 'GAIIpk': 5, 'G@`HmS': 4, 'G@`Hpk': 5, 'G_C\\b[': 4, 'GCd@j[': 5, 'G@LDI{': 5, 'G@MBI{': 4, 'GDGie[': 4, 'GCQaX{': 5, 'GGC]H{': 5, 'G_CZH{': 5, 'GU?Gz[': 4, 'GAHSX{': 5, 'GA`PX{': 5, 'G_F@X{': 4, 'G@UCj[': 5, 'G@_qX{': 5, 'GR?HY{': 4, 'GL?HY{': 4, 'G@MBM{': 4, 'GOC]J{': 4, 'G@`SZ{': 5, 'G@OsZ{': 4, 'G@_qZ{': 4, 'GL?H]{': 4, 'G@_q^{': 4, 'GASo\\C': 6, 'G@`LQg': 6, 'GBOkSK': 6, 'GICW\\C': 5, 'GA[PKK': 6, 'GQSOXK': 6, 'G@O]TG': 6, 'GQCWZC': 5, 'GCdR@[': 6, 'G@Le?{': 5, 'GcCZ@[': 5, 'GgC[`[': 5, 'GHEJ?{': 6, 'GEd@H[': 6, 'GeCHH[': 5, 'GKcQH[': 6, 'GHMAG{': 5, 'G`KaG{': 5, 'GKC]@[': 5, 'GAIao{': 6, 'G@QcYs': 6, 'G@RCXs': 5, 'GBIA[[': 6, 'GGEao{': 5, 'GWD?w{': 5, 'GR?KY[': 5, 'GAIJ_{': 6, 'GGEJ_{': 5, 'GQ?io{': 6, 'G@`KZc': 5, 'G@`P]S': 6, 'G`@KXs': 5, 'GODao{': 5, 'G@MeA{': 5, 'GTGII{': 6, 'GJOKH{': 5, 'GPMAI{': 5, 'G`KcI{': 5, 'GCPcp{': 6, 'GWD?x{': 5, 'G_Dcp{': 5, 'GgE?x{': 5, 'GDHAX{': 6, 'GCOm`{': 6, 'G_Cm`{': 5, 'GK@Kp{': 6, 'GR?IX{': 5, 'GgC_x{': 5, 'GGFCp{': 5, 'GJOKL{': 5, 'G@b@r{': 5, 'GODLb{': 6, 'GWD?z{': 5, 'G@`Lb{': 5, 'GoC_z{': 5, 'GWD?~{': 5, 'G@EIrK': 5, 'GACjc[': 5, 'GAEJ`[': 5, 'G@Ok]c': 5, 'GCSXNC': 5, 'GCGYXk': 5, 'GAIOx[': 6, 'GGCq[[': 5, 'G@`Gw{': 5, 'G@G[Y[': 5, 'GCCivK': 5, 'G?dPj[': 5, 'G?LSj[': 5, 'GC`HZk': 5, 'G@`Oz[': 5, 'GAIOz[': 5, 'GCHOz[': 5, 'GODKZk': 5, 'GCS_~K': 5, 'GA_gx{': 5, 'G_GYX{': 5, 'G@`Gx{': 5, 'GAHKX{': 5, 'G?MQn[': 5, 'GAIO~[': 5, 'GCOgz{': 5, 'G@QGz{': 5, 'GCOkZ{': 5, 'G@`G~{': 5, 'GAMBjW': 5, 'G_G\\rg': 5, 'GQ?{Zs': 5, 'GOPozs': 5, 'GGEsZs': 5, 'GGaozs': 5, 'G_Iozs': 5, 'GHQA|w': 5, 'GQ@Hx{': 5, 'G`?ky{': 5, 'GODJh{': 5, 'GOOXzk': 5, 'G`?Xz[': 5, 'GAMBj[': 5, 'GCOjk{': 5, 'G_Cli{': 5, 'GG_Y|k': 5, 'G_G\\rk': 5, 'GOPo~s': 5, 'GOQPz{': 5, 'GK@Hz{': 5, 'G@Qcz{': 5, 'GOOsz{': 5, 'G`?kz{': 5, 'GHQA|{': 5, 'GK@H~{': 5, 'G@`TZo': 5, 'GGEJrg': 4, 'G@`Jtg': 4, 'G@_}Js': 4, 'GOEqZs': 5, 'GGDsZs': 4, 'G@aqZs': 4, 'GgCa|w': 4, 'G@`a{{': 5, 'G@R@x{': 4, 'GODa{{': 4, 'GGEJh{': 5, 'GCOmh{': 5, 'G_Cmh{': 4, 'G@`TZs': 5, 'G@QJh{': 4, 'GGEJrk': 4, 'G@`Jtk': 4, 'GGDs^s': 4, 'G@b@z{': 4, 'G@`cz{': 5, 'G@R@z{': 4, 'GODcz{': 4, 'GgCa|{': 4, 'G@R@~{': 4, 'G@QTZo': 5, 'G@`Lrg': 5, 'G`?{Zs': 4, 'GOQozs': 5, 'G@QsZs': 5, 'GG`ozs': 4, 'GWDA|w': 4, 'GK?ky{': 5, 'G`@Hx{': 4, 'GCOli{': 5, 'GK?Xz[': 5, 'GG_[zk': 4, 'G@QTZs': 5, 'G@`Jh{': 4, 'G@`Lrk': 4, 'GG`o~s': 4, 'G`AHz{': 4, 'GOO\\j{': 5, 'G@QLj{': 4, 'G`@Hz{': 4, 'GWDA|{': 4, 'G`@H~{': 4, 'GD`@zW': 5, 'G@b@zo': 4, 'G`AHzo': 4, 'G``@xw': 4, 'G@h@}g': 5, 'G`GP}W': 4, 'G@`H~_': 4, 'G`Q@zw': 4, 'GIICzw': 5, 'GWDCzw': 4, 'GD`@z[': 5, 'G@b@zs': 4, 'G`AHzs': 4, 'G``@x{': 4, 'G@h@}k': 5, 'G`GP}[': 4, 'G@`H~c': 4, 'G``@~w': 4, 'G`Q@z{': 4, 'GIICz{': 5, 'GWDCz{': 4, 'G``@~{': 4, 'G@_zMs': 5, 'GCKiZk': 5, 'GAKkZk': 5, 'G@dKZk': 5, 'GOdGzk': 5, 'GK?x]s': 5, 'GCHHx{': 5, 'GCOix{': 5, 'GOOYx{': 5, 'GG_Yx{': 5, 'G@`LY{': 5, 'GCKi^k': 5, 'G@``}{': 5, 'GCHHz{': 5, 'GAIHz{': 5, 'G@QKz{': 5, 'GOO[z{': 5, 'GK?h}{': 5, 'GCHH~{': 5, 'G`?x]s': 4, 'G_Kgzk': 5, 'GGeGzk': 4, 'G_Kg~k': 4, 'G`?h}{': 4, 'G_GXz{': 5, 'GG_[z{': 4, 'G_GX~{': 4, 'GOCzMs': 4, 'GCdHZk': 5, 'G@MIZk': 4, 'G@QIx{': 5, 'G@`H}[': 4, 'G@`Hx{': 4, 'G@MI^k': 4, 'GOD`}{': 4, 'GCOkz{': 5, 'G@`Hz{': 4, 'G@`H~{': 4, 'GKAJzw': 4, 'GQ?Z~W': 5, 'GGENjw': 4, 'GG_Z~g': 4, 'G_G^vg': 4, 'GKAJ~w': 4, 'GKAJz{': 4, 'GQ?Z~[': 5, 'GGENj{': 4, 'GG_Z~k': 4, 'G_G^vk': 4, 'GKAJ~{': 4, 'GCOjzw': 5, 'G_G\\zw': 5, 'GCOj~w': 5, 'GCOjz{': 5, 'G_G\\z{': 5, 'GCOj~{': 5, 'GCHLzw': 5, 'G@QJzw': 4, 'G@`Lzw': 4, 'G@QJ~w': 4, 'GCHLz{': 5, 'G@QJz{': 4, 'G@`Lz{': 4, 'G@QJ~{': 4, 'G@`N~w': 4, 'G@`N~{': 4, 'GGD_kS': 5, 'GCGgYc': 5, 'G@dAHK': 6, 'GG`_gs': 5, 'G_GXeC': 5, 'G@?{QS': 5, 'G@PL?{': 5, 'GGaR?{': 5, 'GOPH_{': 5, 'GIICG{': 5, 'GGC\\?{': 4, 'Gh?GW{': 5, 'GGY?g{': 5, 'GCS`G{': 5, 'GAaJ@{': 5, 'GGC]@{': 4, 'G_CZ@{': 4, 'Gq?GX{': 4, 'GAU@H{': 5, 'G_G]@{': 5, 'G@MAH{': 4, 'GOC]B{': 4, 'GAMCJ{': 5, 'G@MAJ{': 4, 'G@MAN{': 4, 'GGD_sK': 4, 'G@PHc[': 4, 'GAS`K{': 4, 'GGCZC{': 4, 'G@LAL{': 4, 'GJ?G^{': 3, 'GACitK': 6, 'G@EaY[': 5, 'G@E`q[': 5, 'GICG|K': 5, 'G@KqUK': 5, 'GAS_|K': 5, 'G?LQl[': 5, 'G?gpi{': 5, 'G@WPm[': 5, 'GI?W|[': 5, 'GCGgy{': 5, 'GAHO|[': 6, 'G@PH[{': 5, 'G@_pY{': 5, 'GOGWy{': 5, 'GGDO|[': 5, 'G@L@m[': 5, 'G?Wpm{': 5, 'G@PG|{': 5, 'GCGgz{': 5, 'G@Op]{': 5, 'GGOW|{': 5, 'GAGg~{': 5, 'GOCqY[': 5, 'G@_qY[': 4, 'GKCW^C': 4, 'GCGgy[': 5, 'GGDcW{': 5, 'G@aIZc': 4, 'GGEOx[': 5, 'GOCYrK': 5, 'GGCZc[': 4, 'GGEKZk': 4, 'GQ?Wz[': 5, 'GKCG~K': 4, 'GK?Wz[': 4, 'GCHIX{': 5, 'GG_[Zk': 5, 'G@PKX{': 4, 'GODOz[': 5, 'GG_Wx{': 5, 'GGEOz[': 4, 'G_CXvK': 4, 'GK?W~[': 4, 'GGEKZ{': 4, 'GOOWz{': 5, 'GGEO~[': 4, 'GG_Wz{': 4, 'GG_W~{': 4, 'GBGic[': 5, 'G@LBK{': 5, 'GJ?H[{': 5, 'GIS`K{': 4, 'GAHP[{': 5, 'GGCZK{': 4, 'GJ?I\\{': 4, 'G@Oq\\{': 5, 'GGD_~{': 4, 'G@`HuG': 5, 'GASXLC': 5, 'G@aIZ_': 5, 'GG[OkK': 5, 'GBaI`[': 5, 'G`C]@[': 4, 'GPLAG{': 5, 'GWCZ?{': 4, 'Gf?GX[': 4, 'GJ?G{[': 4, 'GHMCI{': 4, 'GWC\\A{': 4, 'G`LAH{': 4, 'GCdBH{': 5, 'Ge?HX{': 4, 'GJ?KX{': 4, 'G@LEH{': 4, 'G_C^@{': 3, 'G`LAL{': 3, 'GT?IZ{': 4, 'G@MEJ{': 4, 'GJ?KZ{': 3, 'GJ?K^{': 3, 'GGCW~C': 4, 'GGCW~K': 4, 'GOCWz[': 4, 'GGCW~[': 4, 'GOCWz{': 4, 'GGCW~{': 3, 'G@LDmW': 4, 'G@UKZk': 4, 'GCShZk': 4, 'GCHp]s': 4, 'GAchZk': 4, 'GOoWzk': 4, 'GCGiy{': 4, 'GCGmi{': 5, 'G@PKx{': 5, 'G@PL[{': 4, 'GOCZj[': 4, 'GCGhy{': 5, 'GGC\\j[': 5, 'GGC]l[': 4, 'G@LDm[': 4, 'GGC]X{': 5, 'GAch^k': 4, 'GAaHz{': 4, 'GCGiz{': 4, 'G@_r]{': 4, 'GAGkz{': 4, 'G_C\\Z{': 4, 'GCGi~{': 4, 'G@aJrg': 5, 'GGDbsw': 4, 'G@`sZs': 5, 'GOF_zs': 4, 'GGF_zs': 4, 'GJ?M\\w': 4, 'GGDc{{': 4, 'G@PLh{': 5, 'G@aJrk': 5, 'GGDbs{': 4, 'GGF_~s': 4, 'GOEaz{': 5, 'G@_uZ{': 4, 'GGDcz{': 4, 'GJ?M\\{': 4, 'GGDc~{': 4, 'G@LI\\k': 4, 'GASh\\k': 5, 'G@Pq\\s': 4, 'G@LI^k': 4, 'G@PH|{': 4, 'GAGi|{': 5, 'GGDa|{': 4, 'G@PH~{': 4, 'GAKh]k': 5, 'GPCWz[': 4, 'GICW|[': 4, 'GGCX~K': 5, 'GHCW~[': 4, 'GAGh}{': 5, 'GOCXz{': 4, 'GGCY|{': 4, 'GGCX~{': 4, 'GGcW~K': 4, 'GQCWz[': 4, 'GKCWz[': 4, 'G_CZX{': 5, 'GGC[~K': 4, 'GGCZ[{': 4, 'GGC[x{': 4, 'GKCW~[': 3, 'G_CX~[': 4, 'G_CXz{': 4, 'GGC[z{': 3, 'G_CX~{': 3, 'G@PL|w': 4, 'GGC^nW': 4, 'G@PJ|w': 4, 'G@PL~w': 4, 'G@PL|{': 4, 'GGC^n[': 4, 'G@PJ|{': 4, 'G@PL~{': 4, 'GAGl}w': 4, 'GOCZzw': 4, 'GGC\\zw': 4, 'GGC]|w': 4, 'GOCZ~w': 4, 'GAGl}{': 4, 'GOCZz{': 4, 'GGC\\z{': 4, 'GGC]|{': 4, 'GOCZ~{': 4, 'GGCZ~w': 3, 'GGCZ~{': 3, 'GGC^~w': 3, 'GGC^~{': 3, 'G@XRc[': 4, 'G@iRIs': 4, 'G@iQZc': 5, 'GFOjC[': 4, 'GAWpk[': 4, 'GGUJ`k': 5, 'G@Q\\Rc': 5, 'G@Ycqk': 4, 'G@`io{': 5, 'GOOwzc': 5, 'G@_rYw': 4, 'G@`[jS': 5, 'G@PL[w': 4, 'GGaQxw': 5, 'GALfC{': 4, 'GBOmH{': 4, 'GP_ZI{': 4, 'GOMRI{': 4, 'GYD@[{': 4, 'G@iRI{': 4, 'GAMJH{': 4, 'G@`ip{': 5, 'G`@ip{': 5, 'GAqPX{': 5, 'GG_|a{': 4, 'G_dPX{': 5, 'GGEtQ{': 5, 'GBOmL{': 4, 'G@XSZ{': 4, 'GCMaZ{': 4, 'G@iQZ{': 4, 'G`@it{': 4, 'G@XS^{': 4, 'GIL_sK': 5, 'G@hSZc': 5, 'GBQJPk': 5, 'GLX?k[': 5, 'GBOp[[': 5, 'G@PtSs': 5, 'G@U`i[': 5, 'G@LTMS': 5, 'G@dKjK': 5, 'G@crI[': 5, 'G@XSk[': 5, 'GAoph[': 5, 'GAIZbS': 5, 'G@Pko{': 5, 'G@`LYw': 5, 'GAI[jS': 5, 'GGoWxk': 5, 'G@Qgzc': 5, 'GGD[lS': 5, 'G@Qio{': 5, 'G@Qhis': 5, 'GAaXjS': 5, 'G@Ox]c': 5, 'GaKbK{': 5, 'GP_qY{': 5, 'GPEaY{': 5, 'GIDcX{': 5, 'G@guI{': 5, 'GJOLK{': 5, 'GGgsi{': 5, 'GGMTI{': 5, 'G_Wqh{': 5, 'GW_oy{': 5, 'GiC`[{': 5, 'GCpHh{': 5, 'GAcjH{': 5, 'G_cZH{': 5, 'G@arQ{': 5, 'G@hIh{': 5, 'GAeJH{': 5, 'GOErQ{': 5, 'GAKmH{': 5, 'GGDuP{': 5, 'G@_~A{': 5, 'GIDc\\{': 5, 'G_Wql{': 5, 'GCgij{': 5, 'G@iIj{': 5, 'GAWkj{': 5, 'GOK]J{': 5, 'GGDuT{': 5, 'GAWkn{': 5, 'G?MreO': 4, 'G@MamO': 5, 'G@Y\\Ac': 4, 'GQLe?{': 4, 'GqL@G{': 4, 'GCR`ps': 4, 'G@b`qs': 5, 'G`Ahqs': 5, 'GDU@ZK': 4, 'G@`huc': 5, 'G@h_}c': 4, 'GAG[~G': 5, 'GG_Y|g': 5, 'GGC]lW': 4, 'GAG]\\g': 5, 'GR`M@{': 4, 'GhQ?x{': 4, 'GiGSX{': 4, 'GMHCX{': 4, 'GCO~@{': 4, 'G@Qm`{': 5, 'G_ErP{': 5, 'GCQj`{': 4, 'GqI?z{': 4, 'GA`lb{': 4, 'GGFTR{': 4, 'GGFTV{': 4, 'G@ejQk': 4, 'GCOxzo': 4, 'GCSxZc': 5, 'GALmTk': 4, 'GBSkj[': 4, 'GDcij[': 4, 'GDMIj[': 4, 'G_[ilk': 4, 'GA\\c\\k': 4, 'G@URZ[': 4, 'G@dTZ[': 4, 'GCLTZ[': 4, 'GBSkn[': 4, 'GAZ@|{': 4, 'G@URZ{': 4, 'GCLLj{': 4, 'G@dLj{': 4, 'G_WZl{': 4, 'GAYJl{': 4, 'G@UR^{': 4, 'GAMjSk': 5, 'GCdXrK': 4, 'GCSxjS': 5, 'GGD}dS': 4, 'G_Litk': 4, 'GDcqZ[': 5, 'GBSsZ[': 4, 'GA[mLk': 4, 'GCSrZ[': 4, 'GBSs^[': 4, 'G_XP|{': 4, 'GCH\\r{': 4, 'GCSrZ{': 4, 'GGoZl{': 4, 'GCSr^{': 4, 'GCO~fO': 4, 'G@`i~_': 4, 'G@P^Lo': 5, 'GG`ytc': 4, 'G[@[Zs': 4, 'GCxHjk': 4, 'G@tcZk': 4, 'G@xKjk': 4, 'GC\\LJk': 4, 'GQBkrs': 4, 'GR?Z][': 4, 'GGMJmk': 4, 'GGoZlk': 4, 'GOoZjk': 4, 'GCO~fS': 4, 'GCLH~K': 4, 'GCHX~S': 5, 'G@hH}k': 5, 'G@yInk': 4, 'GkAHz{': 4, 'G_W\\j{': 4, 'GAYLj{': 4, 'GGo\\j{': 4, 'GOoZj{': 4, 'GKBLr{': 4, 'GOoZn{': 4, 'G@MYvK': 4, 'GCOzp{': 4, 'GCSsz[': 5, 'GCOxx{': 4, 'G@`Yx{': 5, 'GAI[z[': 5, 'G@dP~[': 4, 'GCOxz{': 4, 'GAI[z{': 4, 'GOOx}{': 4, 'GCOx~{': 4, 'GAMXvK': 5, 'GCKizk': 5, 'GCSjh{': 5, 'G@USz[': 5, 'GAcjh{': 5, 'GAIXx{': 5, 'GAHX{{': 5, 'GGEhy{': 5, 'G@Qhy{': 5, 'G@cq~[': 5, 'GAcp~[': 5, 'GCHXz{': 5, 'G@`[z{': 5, 'GAIXz{': 5, 'GGEh}{': 5, 'G@Qh}{': 5, 'GAIX~{': 5, 'G_Ww~c': 5, 'GCHizs': 5, 'GAiHzk': 5, 'GCHlq{': 5, 'G_C|Zs': 5, 'G`?~Q{': 5, 'GCOzZs': 5, 'GCLLj[': 5, 'GCH\\r[': 5, 'G_IXzs': 5, 'GOO~a{': 5, 'GOOxy{': 5, 'GODhy{': 5, 'G_Dhx{': 5, 'GCIYz[': 5, 'G_IYx{': 5, 'GGEi{{': 5, 'G@QtY{': 5, 'GOSZ^k': 5, 'G_WX~k': 5, 'G_Dhz{': 5, 'GAahz{': 5, 'GAIkz{': 5, 'G_Ehz{': 5, 'GG`q|{': 5, 'G_Dh~{': 5, 'G@X[^c': 4, 'G@UJZk': 4, 'GChHzk': 4, 'G@Q\\Zs': 4, 'GG_~a{': 4, 'GCLLZk': 4, 'GA_xz[': 4, 'G@_zY{': 5, 'G@`rY{': 5, 'GAJKx{': 5, 'G@Pt[{': 5, 'GAYH~k': 4, 'G@`iz{': 4, 'GCO|Z{': 4, 'G@Qkz{': 4, 'G`@i|{': 4, 'G@`i~{': 4, 'GGow~c': 5, 'GAHls{': 5, 'GAG|u[': 5, 'GCHZt[': 5, 'G@`\\Zs': 5, 'G@QZr[': 5, 'GCJHzs': 5, 'GAI^b[': 5, 'GGFHx{': 5, 'GAHr[{': 5, 'GGS\\^k': 5, 'GGoX~k': 5, 'GCIiz{': 5, 'G@aiz{': 5, 'GGFHz{': 5, 'GOC}Z{': 5, 'GGDu\\{': 5, 'GGFH~{': 5, 'GGFT^o': 4, 'GQAZr[': 4, 'GAIZvK': 4, 'GK?zu[': 4, 'GCOx~K': 4, 'G@O|]k': 5, 'G_C|j[': 5, 'GA_|j[': 4, 'GQBH~s': 4, 'GA`lj{': 4, 'GGFTZ{': 4, 'GGFT^{': 4, 'G@dV^W': 4, 'G@dV^w': 4, 'G@dV^[': 4, 'G@dV^{': 4, 'GAMR~W': 4, 'GA`x~s': 4, 'GAMR~[': 4, 'GA_zz{': 4, 'GCO|z{': 4, 'GCH\\z{': 4, 'GA_z~{': 4, 'GAIZ~o': 4, 'GAH{~s': 4, 'GAIZ~s': 4, 'GAIZz{': 4, 'GAIZ~{': 4, 'G@`^^o': 4, 'GCRh~s': 4, 'G@`^^s': 4, 'GCOz~[': 4, 'GG_z}{': 4, 'G@Q^Z{': 4, 'G_IZz{': 4, 'GCO~n[': 4, 'G_IZ~{': 4, 'GCO~~w': 4, 'GCO~~{': 4, 'G@Qhqk': 5, 'G@`[rK': 5, 'G@_zIs': 5, 'G@Oi{w': 5, 'GCKhYk': 5, 'GOWoyk': 5, 'G@YHik': 5, 'GCOixw': 5, 'GAMSZK': 5, 'G@PKxw': 5, 'G@G{Ys': 5, 'G@QIxw': 5, 'G?dXpk': 5, 'GGEpu[': 5, 'GGgXi{': 5, 'G@`[r[': 5, 'GOWXi{': 5, 'GR?g}[': 5, 'GHE_}[': 5, 'G@hHi{': 5, 'GCH[r[': 5, 'G@YHi{': 5, 'G@Mam[': 5, 'GAUPX{': 5, 'GCSpX{': 5, 'GGgXm{': 5, 'G@hHm{': 5, 'GCSpZ{': 5, 'GAMSZ{': 5, 'GCSp^{': 5, 'G@O|Is': 5, 'GBOrS[': 5, 'G@MJIk': 5, 'GAHrS{': 5, 'GGWXk{': 5, 'G@XHk{': 5, 'GGXPk{': 5, 'GIHP[{': 5, 'GASp[{': 5, 'GAHit{': 5, 'GASp\\{': 5, 'GASp^{': 5, 'GG_Yxw': 5, 'G@O{Zc': 4, 'GALbK{': 4, 'GIGg{{': 4, 'GGLRK{': 5, 'GBGi[{': 4, 'GAWhk{': 5, 'GGDXs{': 4, 'GGDrS{': 4, 'GBHI\\{': 4, 'GICX\\{': 4, 'G@XQ\\{': 5, 'GGDXv{': 4, 'G@K|a[': 4, 'GCKze[': 4, 'GHK\\I{': 4, 'GBchm[': 5, 'GPKZI{': 4, 'GLCX][': 4, 'G@May{': 4, 'GOCyzs': 4, 'GPKZM{': 4, 'G@Ma}{': 4, 'G@Maz{': 4, 'G@cr]{': 5, 'G@Lcz{': 4, 'GPCZ]{': 4, 'G@Ma~{': 4, 'G@d[rK': 5, 'GAsph[': 5, 'GASxlS': 5, 'GAhitk': 5, 'GEchj[': 5, 'GBeHj[': 5, 'GDPXr[': 5, 'GAsjLk': 5, 'GAwilk': 5, 'G@LT][': 5, 'GALT\\[': 5, 'GGWq{{': 5, 'GGK]nK': 5, 'GGW]lk': 5, 'GCUPz[': 5, 'GAG}p{': 5, 'GAKl]k': 5, 'G@LL]k': 5, 'G@aZZs': 5, 'G@TJ\\k': 5, 'GGC~e[': 5, 'GDPXv[': 5, 'GGXS|{': 5, 'G@cuZ{': 5, 'GCcrZ{': 5, 'GAStZ{': 5, 'GAWml{': 5, 'GGW]l{': 5, 'GASt^{': 5, 'G@TZd[': 4, 'GHKZK{': 4, 'GBTHl[': 5, 'GJCY\\[': 4, 'G@Lcy{': 4, 'GHPH{{': 4, 'GAKkzk': 5, 'GGC{zs': 4, 'G@Pjs{': 5, 'GHKZM{': 4, 'GAT`|{': 4, 'G@La|{': 4, 'GASjl{': 5, 'GICZ\\{': 4, 'G@La~{': 4, 'GBhI\\k': 4, 'GUCXZ[': 4, 'G@ta\\k': 5, 'GMCXZ[': 4, 'GRC[Z[': 4, 'GBGk}[': 4, 'GIC\\\\[': 4, 'GAKk~K': 5, 'GGC}p{': 4, 'GGD[|s': 4, 'GMCX^[': 4, 'GHPK|{': 4, 'GPC]Z{': 4, 'G@XMl{': 5, 'GIC\\Z{': 4, 'GSCZZ{': 4, 'GIC\\^{': 4, 'G@Kze[': 4, 'G@M`y{': 4, 'G@L`}{': 4, 'G@_xz{': 4, 'GAGx}{': 5, 'GGCx}{': 4, 'G@Ox~{': 4, 'GALXvK': 5, 'GASlh{': 5, 'GAKi|k': 5, 'GGWY|k': 5, 'GGSZ\\k': 5, 'GASp~[': 5, 'GAHX|{': 5, 'GGDi|{': 5, 'GAHX~{': 5, 'GIKW~K': 4, 'GGD\\p{': 4, 'GGCy|s': 4, 'GICX~[': 4, 'GGDX|{': 4, 'G@Pi|{': 5, 'GGDX~{': 4, 'G@Le}w': 4, 'G@Ld}w': 4, 'GGC}~o': 4, 'G@Le~w': 4, 'G@Le}{': 4, 'G@Ld}{': 4, 'GGC}~s': 4, 'G@Le~{': 4, 'G@Qx~s': 4, 'G@_zz{': 4, 'G@_z~{': 4, 'G@Su~W': 5, 'GAJX~s': 5, 'G@Su~[': 5, 'GCG}z{': 5, 'G@P\\|{': 5, 'GAG}z{': 5, 'GGC~]{': 5, 'G@O~]{': 5, 'GAH\\~{': 5, 'G@LNjw': 4, 'G@Px~s': 4, 'G@LNj{': 4, 'G@O|z{': 4, 'GGC}z{': 4, 'G@Oz~{': 4, 'GGFX~s': 4, 'GGC}|{': 4, 'GGD\\|{': 4, 'GGD\\~{': 4, 'G@O~~w': 4, 'G@O~~{': 4, 'G@ddQk': 5, 'GHXSc[': 5, 'G@cjIk': 5, 'G_Sph[': 5, 'G@dSZK': 5, 'GGMQk[': 5, 'G@hcqk': 5, 'GGg[ik': 5, 'G@`\\Rc': 5, 'GOSpi[': 5, 'GCWhik': 5, 'G@]BIk': 5, 'GCYQh[': 6, 'GGdPk[': 5, 'GGcYlK': 5, 'G@`tQs': 5, 'G_C|bS': 5, 'GCPgxs': 5, 'GOPWxs': 5, 'GOOxis': 5, 'GOWWyk': 5, 'G@_jiw': 5, 'G`?xYs': 5, 'G@O]\\W': 5, 'GCH[jS': 5, 'GG_q{w': 5, 'GGEYlS': 5, 'GEWbK{': 5, 'GAorH{': 5, 'G@YTI{': 5, 'GOWsi{': 5, 'GoGXi{': 5, 'GMO`[{': 5, 'GI`_x{': 5, 'GPQ_y{': 5, 'GPOsY{': 5, 'G`GsY{': 5, 'GJQ@[{': 5, 'GCLJH{': 5, 'GCHip{': 5, 'G_Kih{': 5, 'GG`qp{': 5, 'G@qIh{': 5, 'GGeIh{': 5, 'GOQpq{': 5, 'GGc]H{': 5, 'G@QtQ{': 5, 'G`?|Q{': 5, 'GAorL{': 5, 'GI`_|{': 5, 'GCXHj{': 5, 'GAiHj{': 5, 'GAgkj{': 5, 'G_Kkj{': 5, 'GG`qt{': 5, 'GCXHn{': 5, 'GKOW|K': 5, 'GHQGw{': 5, 'GQGgw{': 5, 'G`Ogw{': 5, 'GPOoy[': 6, 'GKOgw{': 5, 'GCKgzK': 5, 'G@_za[': 5, 'GKCWx[': 5, 'GGHW{s': 5, 'G@Qpq[': 5, 'GGEYtK': 5, 'GOSpm[': 5, 'GDGiY{': 5, 'G@U`m[': 5, 'GBGkY{': 5, 'GSOWz[': 5, 'GKGgy{': 5, 'GPOo}[': 5, 'GQGgy{': 5, 'G`_Wz[': 5, 'GCWhi{': 5, 'GKCXX{': 5, 'GaCXX{': 5, 'GAghi{': 5, 'GOS[j[': 5, 'G@Qpu[': 5, 'GIC[X{': 5, 'GBGk]{': 5, 'GQGg}{': 5, 'GQCXZ{': 5, 'GAghm{': 5, 'GKCXZ{': 5, 'GQC[Z{': 5, 'GKCX^{': 5, 'GK_WzK': 4, 'G`CpY[': 5, 'GGc[jK': 4, 'GOGYyw': 5, 'G`?xq[': 4, 'GGE[rK': 4, 'G_Kpm[': 3, 'G`Ggy{': 4, 'G`Cp][': 4, 'GK_Wz[': 4, 'G_Gxq{': 5, 'GODYp{': 4, 'GGE[r[': 4, 'G`?xu[': 3, 'G`Gg}{': 3, 'G_Cxr{': 4, 'G_Gxu{': 4, 'GGE[r{': 3, 'G_Cxv{': 3, 'GB\\@KK': 5, 'G@NDa[': 5, 'GJAJO{': 5, 'GLPHc[': 4, 'GCdPZK': 5, 'GASp\\K': 5, 'G@aZRc': 5, 'G@KZMK': 5, 'G@LLeK': 5, 'GJ?ZS[': 4, 'G@opi[': 4, 'GGEZbS': 5, 'G@pGxk': 6, 'G@`H}W': 4, 'GCQXjS': 5, 'GGWW{k': 4, 'G@QpYs': 5, 'GGE[jS': 4, 'G@OxmS': 5, 'GQSbK{': 4, 'GT?iY{': 5, 'G@MeI{': 4, 'GJ@KX{': 4, 'GISdK{': 4, 'GH_sY{': 5, 'GWC\\I{': 5, 'G`OqX{': 5, 'Gj?H[{': 4, 'GCdJH{': 5, 'GAgih{': 5, 'G_oXh{': 4, 'GCIrQ{': 5, 'G@LMH{': 5, 'GOC~A{': 4, 'G@PuP{': 4, 'GJ@K\\{': 4, 'G`Oq\\{': 4, 'GOgYj{': 5, 'G@MMJ{': 4, 'GGW[j{': 4, 'G@PuT{': 4, 'GGW[n{': 4, 'G@iZAc': 6, 'G@MqUC': 5, 'GQTd?{': 5, 'GqS`G{': 4, 'GCl@jK': 6, 'G@bHrc': 5, 'G`BHps': 4, 'G@l@mK': 5, 'G`KHmK': 4, 'GAG]lW': 6, 'GG_[zg': 5, 'GGC[~G': 4, 'GTPM@{': 4, 'GwD?x{': 5, 'GJQCX{': 5, 'Gj?KX{': 4, 'GCQrP{': 6, 'G@QuP{': 5, 'G`?}P{': 4, 'GwE?z{': 4, 'GG`sr{': 5, 'GGFcr{': 4, 'GGFcv{': 4, 'GKLI\\k': 4, 'GRCYZ[': 4, 'GC\\a\\k': 5, 'GLC[Z[': 4, 'GdCXZ[': 4, 'GKGiy{': 4, 'GKC\\Z[': 5, 'G`C\\Z[': 4, 'GRCY^[': 4, 'GKPH|{': 4, 'GQCZZ{': 4, 'GCXJl{': 5, 'GKC\\Z{': 4, 'G`C\\Z{': 4, 'GQCZ^{': 4, 'G_C~fO': 4, 'GG`q|o': 5, 'GG`zcs': 4, 'G@Pu\\o': 4, 'GK`sZs': 4, 'GClJJk': 5, 'G@]MJk': 4, 'GGw[jk': 4, 'GGbsrs': 4, 'GOSZnK': 5, 'GGeJjk': 4, 'GGcZnK': 4, 'G_C~fS': 4, 'GCHh}s': 5, 'G_Kh}k': 4, 'G@]MNk': 4, 'G`b@z{': 4, 'GCXLj{': 5, 'G@qJj{': 4, 'G@pLj{': 4, 'G`BLr{': 4, 'GGeJn{': 4, 'GGD~Cs': 4, 'G`LI\\k': 4, 'GTCYZ[': 5, 'G@\\MLk': 4, 'GJC[Z[': 4, 'GKCZZ[': 4, 'GJC[^[': 4, 'G`PH|{': 4, 'GOD\\r{': 5, 'G@pJl{': 4, 'GKCZZ{': 4, 'GKCZ^{': 4, 'GKKW~K': 4, 'GODXzs': 4, 'GKCXz[': 5, 'GGEY|s': 4, 'GGEXx{': 4, 'GGDh{{': 5, 'GGDX{{': 4, 'GPCY~[': 4, 'GKCX~[': 4, 'GODXz{': 4, 'GAIh}{': 5, 'GGEXz{': 4, 'GOD[z{': 4, 'GGEX~{': 4, 'G`KW~K': 3, 'G_Czp{': 4, 'GGE[zs': 4, 'GODYx{': 4, 'GGDk{{': 4, 'G`CX~[': 3, 'G_Cxz{': 4, 'G_Gx}{': 4, 'GGE[z{': 3, 'G_Cx~{': 3, 'GGYW~c': 4, 'GAH\\t[': 5, 'G@LLm[': 4, 'GGWZk{': 4, 'G@O~e[': 4, 'GCHjs{': 5, 'G@bHzs': 4, 'GGEZr[': 4, 'GGE^b[': 4, 'G@Ox}[': 4, 'GGDr[{': 4, 'GGW[~k': 4, 'GGcZ^k': 4, 'GOEiz{': 5, 'G@_}Z{': 4, 'GGDkz{': 4, 'G@Pu\\{': 4, 'GGDk~{': 4, 'GGFc~o': 3, 'GKAZr[': 4, 'G`?zu[': 4, 'GGEZvK': 4, 'GCO|j[': 5, 'G@O|m[': 4, 'G`?x}[': 3, 'G`BH~s': 3, 'GG`sz{': 4, 'GGFcz{': 3, 'GGFc~{': 3, 'G`C^^W': 3, 'GKC^^w': 3, 'G`C^^[': 3, 'GKC^^{': 3, 'GQCZ~W': 4, 'G_Dx~s': 4, 'GQCZ~[': 4, 'G_Czz{': 4, 'GOD\\z{': 4, 'G_C|z{': 4, 'G_Cz~{': 4, 'G@RL~o': 4, 'G_Fh~s': 4, 'G@RL~s': 4, 'G_C~Z{': 5, 'GGaZz{': 4, 'GGE^Z{': 4, 'G`?~]{': 4, 'GGaZ~{': 4, 'GGEZ~o': 3, 'GGD{~s': 3, 'GGEZ~s': 3, 'GGEZz{': 3, 'GGEZ~{': 3, 'G_C~~w': 3, 'G_C~~{': 3, 'GIK|e[': 4, 'G@`zrs': 4, 'G@`Zzw': 4, 'G@_zzw': 4, 'GODZzw': 4, 'GAH\\|w': 5, 'GOFJzw': 4, 'GG`zs{': 4, 'GGD\\|w': 4, 'GHMa}{': 4, 'G@`zr{': 4, 'GA`zt{': 4, 'G@Q|r{': 4, 'G_Dzt{': 4, 'G@`zv{': 4, 'GDYYvK': 4, 'GAazrs': 4, 'GBUR\\[': 4, 'GAJZts': 4, 'G@`~Us': 4, 'G@b^Rs': 4, 'GCO|zw': 4, 'GCJXzs': 5, 'GOFizs': 5, 'GG`y|s': 4, 'GGFi|s': 5, 'GAI^nW': 4, 'GDUR^[': 4, 'GA`|r{': 4, 'GAJ\\r{': 4, 'G_Flr{': 4, 'GAJ\\v{': 4, 'GQKze[': 4, 'G@P|ts': 4, 'GAH}ts': 4, 'G@\\Ljk': 4, 'GGD}ts': 4, 'G@`|rs': 4, 'G@lJjk': 4, 'GAI\\zw': 4, 'G@Qxzs': 4, 'GGE\\zw': 4, 'GAHy|s': 5, 'GGFJ|w': 4, 'GGFjs{': 4, 'GGDy|s': 4, 'GHLc}{': 4, 'GPLa}{': 4, 'G@azr{': 4, 'GAJZt{': 4, 'G@Qzr{': 4, 'GGFZt{': 4, 'G@Qzv{': 4, 'GMgW~K': 4, 'GOFZrs': 4, 'GGFZts': 4, 'GRCZ][': 4, 'GODj}w': 4, 'GGFX|s': 4, 'G_C|zw': 4, 'GGDm|w': 5, 'GGE^nW': 4, 'GUCZ^[': 4, 'GOD}r{': 4, 'GGb\\r{': 4, 'GGF\\r{': 4, 'GGF\\v{': 4, 'G@`~vo': 4, 'G@`z~o': 4, 'GAJ\\~o': 4, 'G@Qz~o': 4, 'GGF\\~o': 4, 'G@bzvs': 4, 'G@`~vs': 4, 'G@`~r{': 4, 'G@`~v{': 4, 'G@`zz{': 4, 'GA`z|{': 4, 'G@Q|z{': 4, 'GODz}{': 4, 'G@`z~{': 4, 'GA`~t{': 4, 'GAH}|{': 4, 'GAJ\\~{': 4, 'G@P~t{': 4, 'G@Q~r{': 4, 'G@Qzz{': 4, 'G@Qz~{': 4, 'G_D~t{': 4, 'GGFm|{': 4, 'GGD}|{': 4, 'GGF\\~{': 4, 'G@`~~{': 4, 'GB\\bK{': 3, 'GAHzs{': 4, 'GGDzs{': 3, 'GJPH|{': 3, 'G@Pzt{': 4, 'GGDzv{': 3, 'GGD~vo': 3, 'GGDz~o': 3, 'GGFzvs': 3, 'GGD~vs': 3, 'GGD~v{': 3, 'GGD~r{': 3, 'GGDz~{': 3, 'GGD~~{': 3, 'GGF~vo': 3, 'GGF~vs': 3, 'G@Q~~w': 4, 'GGD~~w': 3, 'GGF~v{': 3, 'GGF~~{': 3, 'G@AiuO': 5, 'GBAI\\O': 5, 'GR?KYW': 5, 'GQAIXo': 5, 'GAND?{': 5, 'GGdT?{': 5, 'GWEQO{': 5, 'GIISO{': 5, 'G@hU@{': 5, 'GCUb@{': 5, 'G_Ma`{': 5, 'GANDB{': 5, 'GqGO^{': 5, 'G@air_': 5, 'G`G\\aW': 5, 'G_C|bO': 5, 'G@hkac': 5, 'G@j?zc': 5, 'GD`HrK': 5, 'G_hPpk': 5, 'G``PXs': 5, 'GIYT?{': 5, 'G@hPuK': 5, 'GCU`rK': 5, 'G_M`is': 5, 'GZOKG{': 5, 'G@j@qk': 5, 'GD``q[': 5, 'GwDPO{': 5, 'GDR@p[': 5, 'GCgYjK': 5, 'GGS[lK': 5, 'GIG[k[': 5, 'GUHAX{': 5, 'GHdEH{': 5, 'GhCMH{': 5, 'GdHAX{': 5, 'GLQAX{': 5, 'G`hU@{': 5, 'GCorH{': 5, 'GChRH{': 5, 'G_gqh{': 5, 'GcOpX{': 5, 'G@UeH{': 5, 'GCUbH{': 5, 'GLQCZ{': 5, 'GChRJ{': 5, 'GGhSj{': 5, 'GANDJ{': 5, 'GANDN{': 5, 'G@ErUO': 5, 'G@Qkr_': 5, 'G?h\\b_': 5, 'G@hP]c': 5, 'GDQHrK': 5, 'G`E`q[': 5, 'GYCm?{': 5, 'GDY?zK': 5, 'G@j@is': 5, 'GBa`q[': 5, 'GYLCG{': 5, 'G`IHis': 5, 'GQ`Hpk': 5, 'GIND?{': 5, 'GWC[i[': 5, 'GYCMH{': 5, 'GLOMH{': 5, 'GkGQX{': 5, 'GbIAX{': 5, 'GcUb@{': 5, 'GMIAX{': 5, 'GCWuH{': 5, 'GAiRH{': 5, 'G_Mah{': 5, 'GQ_qX{': 5, 'G@qah{': 5, 'G`_ih{': 5, 'GUHCZ{': 5, 'GH`Kj{': 5, 'G@pcj{': 5, 'GK`PZ{': 5, 'G_Man{': 5, 'GBOjc[': 5, 'G@iRQk': 5, 'GN@HS[': 5, 'GHQJ_{': 5, 'G@YTQk': 5, 'GCgrI{': 5, 'GGSvC{': 5, 'G@TeH{': 5, 'GOcrI{': 5, 'G@ebI{': 5, 'GYCJK{': 5, 'GIG[X{': 5, 'Ga_XX{': 5, 'GK_pY{': 5, 'GBIIX{': 5, 'G`HQX{': 5, 'GE`HX{': 5, 'GGctI{': 5, 'G@TeL{': 5, 'GSGYZ{': 5, 'GBOkZ{': 5, 'GDIIZ{': 5, 'G`HQ\\{': 5, 'GBOk^{': 5, 'GH_Yk[': 6, 'GJOkc[': 5, 'GQOXh[': 5, 'GIMBG{': 5, 'GK_Yh[': 5, 'G`G\\a[': 5, 'GH_Y[k': 5, 'G``HW{': 5, 'G`OpW{': 5, 'GDQ`Y{': 5, 'GMGJK{': 5, 'GB`aX{': 5, 'GSOpY{': 5, 'GIMBK{': 5, 'G_KtI{': 5, 'GCWtI{': 5, 'GQGYX{': 5, 'G``Gx{': 5, 'GK_YX{': 5, 'G@pah{': 5, 'GoCpY{': 5, 'G`GYX{': 5, 'GB`a\\{': 5, 'GQIGz{': 5, 'G@pal{': 5, 'GKOgz{': 5, 'G`G[Z{': 5, 'GKOg~{': 5, 'G@MimS': 5, 'G@hVMo': 5, 'GCTlRk': 5, 'G@UmRk': 5, 'GGh[rk': 5, 'GCphrk': 5, 'GWbOzs': 5, 'GQb_zs': 5, 'GAj@x{': 5, 'GCh`y{': 5, 'G_M`y{': 5, 'GoGYzk': 5, 'G`EJj[': 5, 'G@j@y{': 5, 'GAiPz[': 5, 'GgEJh{': 5, 'GCL`}[': 5, 'GHEMj[': 5, 'GQGY~K': 5, 'GY?X}[': 5, 'GI_X~K': 5, 'G@hVMs': 5, 'G@VLVk': 5, 'GCZ@z{': 5, 'GAj@z{': 5, 'G@pcz{': 5, 'G_Wsz{': 5, 'Gq?kz{': 5, 'GQ`cz{': 5, 'GAj@~{': 5, 'GGThsk': 5, 'GPcYj[': 5, 'G@TmTk': 5, 'GHS[j[': 5, 'GSKYj[': 5, 'GBXK\\k': 5, 'G`Si\\k': 5, 'GKDHx{': 5, 'GGUP{{': 5, 'GKCix{': 5, 'GKOZX{': 5, 'GQGZ[{': 5, 'GHS[n[': 5, 'GSDHz{': 5, 'G@ZA|{': 5, 'GIEHz{': 5, 'GPDKz{': 5, 'GHQI|{': 5, 'G`HI|{': 5, 'GIEH~{': 5, 'G_K|Qk': 5, 'GAMlIs': 5, 'GCXipk': 5, 'G`cXj[': 5, 'GCXitk': 5, 'GKcXj[': 5, 'GQSXj[': 5, 'GEWi\\k': 5, 'GKXG|k': 5, 'GaChx{': 5, 'GQCix{': 5, 'GQG\\Y{': 5, 'GQSXn[': 5, 'GcChz{': 5, 'GOXQ|{': 5, 'GKCkz{': 5, 'GaChz{': 5, 'GWOY|{': 5, 'GQHI|{': 5, 'GaCh~{': 5, 'G@hVUg': 5, 'GSSiZk': 5, 'GLBKZs': 5, 'GBhKZk': 5, 'GDpHZk': 5, 'GDXKZk': 5, 'G`FcZs': 5, 'GSHHy{': 5, 'GcGXz[': 5, 'GcHHx{': 5, 'GQ_Zj[': 5, 'GIEJl[': 5, 'GWOZk{': 5, 'G@hVUk': 5, 'GDHH}[': 5, 'GD`Hz[': 5, 'GI_Zl[': 5, 'GEIHz[': 5, 'GPOZm[': 5, 'GBhK^k': 5, 'GcHHz{': 5, 'GYAKz{': 5, 'GHQKz{': 5, 'GWO[z{': 5, 'GaIHz{': 5, 'GIacz{': 5, 'GcHH~{': 5, 'GKLKZk': 5, 'GWFSZs': 5, 'GKhGzk': 5, 'GKIHy{': 5, 'G`IHy{': 5, 'GQ`Hx{': 5, 'GQGZm[': 5, 'GI_Z\\k': 5, 'GQGX}[': 5, 'GQMI^k': 5, 'GKQHz{': 5, 'GaIcz{': 5, 'G`Okz{': 5, 'GQ`H~{': 5, 'G@iiqk': 5, 'GGX[tk': 5, 'G@c}b[': 5, 'GAS|b[': 5, 'GCczb[': 5, 'GAXktk': 5, 'GaWg|k': 5, 'GGURX{': 5, 'GCLcz[': 5, 'GEOhx{': 5, 'G@da{{': 5, 'GAMax{': 5, 'G@YRY{': 5, 'GDOjY{': 5, 'G@hTY{': 5, 'GDHLY{': 5, 'GAS|f[': 5, 'GAYa|{': 5, 'GCN@z{': 5, 'GEOhz{': 5, 'GCLcz{': 5, 'GGhQ|{': 5, 'GgGY|{': 5, 'GEOh~{': 5, 'G@hkqk': 5, 'G_Wytk': 5, 'G@mQj[': 5, 'GCkqj[': 5, 'GA[sj[': 5, 'GAW}Tk': 5, 'GISk\\k': 5, 'GCLdY{': 5, 'GCXRX{': 5, 'GCT`x{': 5, 'GCLax{': 5, 'G@YTY{': 5, 'GDHKz[': 5, 'GBQJX{': 5, 'GA[sn[': 5, 'G_Wq|{': 5, 'GD`Hz{': 5, 'GDHKz{': 5, 'GAd`z{': 5, 'GGoq|{': 5, 'GIII|{': 5, 'GAd`~{': 5, 'G@hU^_': 5, 'GAK|UK': 5, 'GALlKs': 5, 'G@MiuK': 5, 'GqAgzs': 5, 'GCX\\Rk': 5, 'G@pkrk': 5, 'GLAJY{': 5, 'GIENH{': 5, 'GY?Y|[': 5, 'GW_Zi{': 5, 'G@hU^c': 5, 'GCN@z[': 5, 'GChPz[': 5, 'G_hPx{': 5, 'G@hP}[': 5, 'G@qivk': 5, 'Gk?kz{': 5, 'G_YPz{': 5, 'GGosz{': 5, 'G_hP~{': 5, 'G?K|rg': 5, 'GHcXm[': 5, 'G@cze[': 5, 'GDKjI{': 5, 'G@hPx{': 5, 'G@MrU{': 5, 'GKCh}{': 5, 'GCL`}{': 5, 'GPDHz{': 5, 'G@hP~{': 5, 'GQEJzw': 5, 'GIEJ|w': 5, 'GQCj}w': 5, 'GQG^]w': 5, 'GQEJ~w': 5, 'GQEJz{': 5, 'GIEJ|{': 5, 'GQCj}{': 5, 'GQG^]{': 5, 'GQEJ~{': 5, 'G@pV\\w': 5, 'GAebzw': 5, 'GANB|w': 5, 'GAYR|w': 5, 'G@hV]w': 5, 'GB`N\\w': 5, 'G@qR~w': 5, 'G@pV\\{': 5, 'GAebz{': 5, 'GANB|{': 5, 'GAYR|{': 5, 'G@hV]{': 5, 'GB`N\\{': 5, 'G@qR~{': 5, 'GPDJzw': 5, 'G@hTzw': 5, 'GPDJ~w': 5, 'GPDJz{': 5, 'G@hTz{': 5, 'GPDJ~{': 5, 'G@hV~w': 5, 'G@hV~{': 5, 'G@Ykqk': 4, 'GAc|b[': 4, 'GAozTk': 4, 'GCSzb[': 4, 'GIog|k': 4, 'GALc{{': 4, 'GALd[{': 4, 'GALcx{': 4, 'GBHL[{': 4, 'G@XT[{': 4, 'G@XR[{': 4, 'GIG]\\k': 4, 'GBOj[{': 4, 'GCSzf[': 4, 'GCMaz{': 4, 'GALe\\{': 4, 'GALcz{': 4, 'GIG]\\{': 4, 'GALc~{': 4, 'GAMjKs': 5, 'GGXXsk': 4, 'GQcXj[': 4, 'G@pitk': 5, 'GKDXr[': 5, 'GBoi\\k': 4, 'GGSs{{': 4, 'GICkx{': 4, 'GIG\\[{': 4, 'GGSr[{': 5, 'GIG]l[': 4, 'GHOZ[{': 4, 'GIG[~K': 4, 'GKDXv[': 4, 'GSCiz{': 4, 'G@XU\\{': 4, 'GGSsz{': 4, 'GBHM\\{': 4, 'GGSs~{': 4, 'G@Xisk': 5, 'G@LrS{': 4, 'GASzd[': 5, 'GISXl[': 4, 'G@LrU{': 4, 'G@XP|{': 4, 'GALa|{': 4, 'GICi|{': 4, 'G@XP~{': 4, 'G@iRzw': 4, 'GALe|w': 4, 'GGSu|w': 4, 'G@XTzw': 4, 'G@XT~w': 4, 'G@iRz{': 4, 'GALe|{': 4, 'GGSu|{': 4, 'G@XTz{': 4, 'G@XT~{': 4, 'GIGZ~w': 4, 'GIGZ~{': 4, 'GIG^~w': 4, 'GIG^~{': 4, 'Gqd`_[': 4, 'G@SmnG': 4, 'GGoylc': 4, 'GChZbK': 5, 'G@h^Ec': 4, 'GII]Tc': 4, 'GBGk}W': 4, 'GBIi[s': 4, 'GHhIkk': 4, 'G@xakk': 4, 'G@tbKk': 4, 'G@Ii}o': 4, 'GAHk|o': 5, 'GGhYlc': 5, 'GAG|uW': 5, 'GALdmW': 4, 'G?S|ug': 4, 'GCpv@{': 4, 'GIEmP{': 4, 'GgSkh{': 4, 'GaLcX{': 4, 'Gq_qX{': 4, 'GKqah{': 4, 'GANeP{': 4, 'GAY^@{': 4, 'G_\\ch{': 4, 'GcQj`{': 4, 'GCoz`{': 4, 'GCTtP{': 4, 'GSW]J{': 4, 'GCNeR{': 4, 'GAY\\b{': 4, 'GAMuR{': 4, 'GAMuV{': 4, 'GALknC': 4, 'GHLI[k': 4, 'GKDXp[': 5, 'GBPhs[': 5, 'GKOixw': 4, 'GBMKZK': 4, 'GH`isk': 5, 'GALi\\c': 4, 'GALk\\c': 4, 'G@TuLS': 5, 'GGD\\pw': 4, 'GBXH[k': 4, 'G?Uxrc': 4, 'G@\\JKk': 5, 'G@aizo': 5, 'GGhqsk': 5, 'G?czjo': 5, 'GODXzo': 4, 'GCHizo': 5, 'GAMi\\c': 5, 'GBXLK{': 4, 'GHp_{{': 4, 'GIUPX{': 4, 'GPcqY{': 5, 'GHYIk{': 5, 'G`Wik{': 4, 'G@xak{': 4, 'GMDHX{': 4, 'GSKZI{': 4, 'GHhIk{': 4, 'GhOg{{': 4, 'GAppp{': 4, 'GDMJI{': 4, 'GGhZc{': 4, 'GWPXs{': 4, 'G@drP{': 4, 'GAdrP{': 4, 'G_Sz`{': 4, 'GDMaY{': 5, 'GGc|a{': 4, 'GOXZc{': 4, 'GIUP\\{': 4, 'GMDH\\{': 4, 'GAppt{': 4, 'G@drR{': 4, 'GDMaZ{': 4, 'GAdrT{': 4, 'G_Szd{': 4, 'G@drV{': 4, 'G@h]vK': 4, 'GAYZls': 4, 'G@VRt[': 4, 'GAerr[': 4, 'G@Zc}s': 4, 'GD\\S^K': 4, 'GAMr][': 4, 'GANdm[': 4, 'GANLh{': 4, 'GDUJn[': 4, 'GOfRZ{': 4, 'GAdlj{': 4, 'GAMuZ{': 4, 'GAMu^{': 4, 'GGS}ls': 4, 'GALmtk': 4, 'G@\\TZk': 4, 'G@iqzs': 4, 'GA\\c|k': 4, 'GRKZM[': 4, 'GHDY|[': 4, 'G@XZk{': 4, 'GDHZr[': 4, 'G@hZtk': 4, 'GHLT]{': 4, 'GGVP|{': 4, 'GANJl{': 4, 'G@Ujj{': 4, 'G@iqz{': 4, 'GAYZl{': 4, 'GRCj]{': 4, 'G@Ujn{': 4, 'GPDZr[': 4, 'GJKkm[': 4, 'GCLr][': 4, 'GGMY|k': 4, 'GPFJY{': 4, 'GCMZj[': 5, 'G@duZ[': 4, 'G@czj[': 4, 'GDIYz[': 4, 'G@h\\rk': 4, 'GHMR]{': 4, 'G_Szl{': 4, 'GAdr\\{': 4, 'G@UtZ{': 4, 'G@drZ{': 4, 'GApp|{': 4, 'GLCj]{': 4, 'G@dr^{': 4, 'GBQk~S': 4, 'G@Vd]s': 4, 'GBQjs{': 4, 'G@uazk': 4, 'GBeaz[': 4, 'GClZfK': 4, 'GHFLY{': 4, 'GD`jY{': 4, 'GBI]^S': 4, 'G@h^Uk': 4, 'GAY\\h{': 4, 'GBQZt[': 4, 'GANJls': 4, 'GBf@~[': 4, 'GSDmZ{': 4, 'GCNeZ{': 4, 'GAY\\j{': 4, 'GAo|j{': 4, 'GChZj{': 4, 'G@uRn[': 4, 'GChZn{': 4, 'G@h]vG': 4, 'G@Mr]o': 4, 'GRFKr[': 4, 'GFJKr[': 4, 'GXMQY{': 4, 'GIFH|s': 4, 'GRCi}[': 4, 'GRG]][': 4, 'G@hX~c': 4, 'GXMQ]{': 4, 'GUEJZ{': 4, 'GEMNJ{': 4, 'GRG]Z{': 4, 'GRG]^{': 4, 'G@Uhzk': 4, 'G@Y]h{': 4, 'G@K|Y{': 4, 'G@Mr]{': 4, 'GPCz]{': 4, 'G@YX}{': 4, 'G@gyz{': 4, 'G@Mi~{': 4, 'G@h^vg': 4, 'G@jq~s': 4, 'GPDm}{': 4, 'G@Y^j{': 4, 'G@hZ~k': 4, 'G@h^vk': 4, 'GPDm~{': 4, 'G@ui~k': 4, 'GAdnl{': 4, 'GCozz{': 4, 'G@h]z{': 4, 'G@Y]z{': 4, 'G@h^]{': 4, 'GAo|~k': 4, 'GCoz~{': 4, 'G@]i~k': 4, 'G@hZz{': 4, 'G@h\\z{': 4, 'G@hZ~{': 4, 'G@h^~w': 4, 'G@h^~{': 4, 'G@pjck': 5, 'GKPgxs': 5, 'GJ`H[k': 5, 'GBMLI[': 5, 'GDXIXk': 5, 'GOTXpk': 5, 'GAMkZc': 5, 'GG\\Hkk': 5, 'GALuLS': 5, 'G@\\TMK': 5, 'GKCXzW': 5, 'GHXG{k': 5, 'GJOg{[': 5, 'G?Upzo': 5, 'G@Qkzo': 5, 'G@XY\\c': 5, 'G`XHk{': 5, 'GWWYk{': 5, 'GKcpY{': 5, 'GaSpX{': 5, 'G@pjc{': 5, 'GTCiY{': 5, 'GIcZH{': 5, 'GHpHk{': 5, 'GJOk[{': 5, 'GDcjI{': 5, 'GAsrH{': 5, 'GGxPk{': 5, 'G@lah{': 5, 'GaSp\\{': 5, 'GIcZL{': 5, 'GAsrL{': 5, 'GTGYZ{': 5, 'G@laj{': 5, 'G@lan{': 5, 'G@XZc[': 4, 'GALrS{': 4, 'GGSzc{': 4, 'GISp[{': 4, 'G@XZd{': 4, 'GIL_~{': 4, 'GILrS{': 4, 'GHTa|{': 4, 'GBOz\\{': 4, 'G@Tr\\{': 4, 'GALr^{': 4, 'GA\\c|g': 4, 'G@LzeS': 4, 'G@Lr]o': 4, 'GPTjc{': 4, 'GWLZc{': 4, 'GXLQ[{': 4, 'G`XZ`{': 4, 'GBT`|[': 4, 'GILc{{': 4, 'G`XZd{': 4, 'GHTc|{': 4, 'GBLe\\{': 4, 'GJG]\\{': 4, 'GILcz{': 4, 'GILc~{': 4, 'GCSzl[': 4, 'GAM\\j[': 4, 'G@dqz[': 4, 'G@fbY{': 4, 'GBIY~S': 4, 'GALr[{': 4, 'GALs~S': 4, 'G@YYx{': 4, 'G@hky{': 4, 'GCLq~[': 4, 'GALs~[': 4, 'GCgyz{': 4, 'G@iYz{': 4, 'G@X[z{': 4, 'GALm\\{': 4, 'GBH[~[': 4, 'G@X[~{': 4, 'G@L^b[': 4, 'G@MZj[': 4, 'G@XX~c': 4, 'G@Lr]{': 4, 'GHCz]{': 4, 'GATh|{': 4, 'G@Li|{': 4, 'G@Li~{': 4, 'GGS~vg': 4, 'GBRh~s': 4, 'GHP\\|{': 4, 'GHOz}{': 4, 'GGS~vk': 4, 'GHP\\~{': 4, 'GAkz^k': 4, 'GHD\\~[': 4, 'GALl|{': 4, 'G@X]|{': 4, 'GALlz{': 4, 'GGS}|{': 4, 'GBO|~[': 4, 'GALl~{': 4, 'G@li~k': 4, 'G@X\\~k': 4, 'G@X\\|{': 4, 'G@X\\z{': 4, 'G@X\\~{': 4, 'G@\\i~k': 4, 'G@XZ~{': 4, 'G@X^~w': 4, 'G@X^~{': 4, 'G`hcyw': 4, 'G@hZtg': 4, 'GATltg': 5, 'G@d^VG': 4, 'GISs|W': 4, 'GPU]b[': 4, 'GLMaY{': 4, 'GDUmb[': 4, 'GPdrQ{': 4, 'GUK]J[': 4, 'GULKj[': 4, 'GHeay{': 4, 'GBqR\\[': 4, 'GQLa{{': 4, 'GLO\\][': 4, 'GKSu\\[': 4, 'GAYq|s': 4, 'GIEi|s': 4, 'GHUle{': 4, 'GQqPz{': 4, 'GHeaz{': 4, 'GDVDZ{': 4, 'GPTcz{': 4, 'GdO\\Z{': 4, 'G`UTZ{': 4, 'GHea~{': 4, 'GBplSk': 4, 'GALmtg': 4, 'G@Tmtg': 5, 'GALs~O': 4, 'GAK}vG': 5, 'G@h^Ug': 4, 'GpS[j[': 4, 'GDY]b[': 4, 'GLKmI{': 4, 'GPLuQ{': 4, 'GDVcr[': 4, 'GUW[j[': 4, 'GXEIy{': 4, 'GYCi{{': 4, 'GFOm\\[': 4, 'GHMuU{': 4, 'GqEHz{': 4, 'GBqTZ{': 4, 'GXEIz{': 4, 'GXDKz{': 4, 'GFQLZ{': 4, 'GbELZ{': 4, 'GXEI~{': 4, 'G_Kzrg': 4, 'GAX{tc': 5, 'GAL{vC': 4, 'G`LrS{': 4, 'GHdrS{': 5, 'GHLuS{': 4, 'GJXSX{': 4, 'G`XPx{': 4, 'GJXS\\{': 4, 'G`XP|{': 4, 'GPTa|{': 4, 'GXDI|{': 4, 'G`XPz{': 4, 'G`XP~{': 4, 'GDLje[': 4, 'G@Tmtk': 4, 'G@Xtq{': 4, 'GGS}tk': 4, 'GISs|[': 4, 'GBe`z[': 4, 'GBJI|s': 4, 'GPXPy{': 4, 'GGNQ|s': 4, 'GIIY|s': 4, 'GBOx|[': 4, 'GIHX{{': 4, 'GBLd]{': 4, 'GPT`}{': 4, 'GP_yz{': 4, 'GBH]\\{': 4, 'GBO|Z{': 4, 'GGNQ|{': 4, 'GIH[|{': 4, 'GBO|^{': 4, 'GKdXvK': 4, 'GPUJi{': 4, 'GBJM\\s': 4, 'GIIZs{': 5, 'GII[x{': 4, 'GcOxx{': 4, 'G`dP~[': 4, 'GP`Yz{': 4, 'GPFMZ{': 4, 'GII[z{': 4, 'GII[~{': 4, 'G`iRzw': 4, 'G`XT~w': 4, 'G`iRz{': 4, 'G`XT~{': 4, 'GDTd~W': 4, 'GP`y~s': 4, 'GDTd~[': 4, 'GP`Zz{': 4, 'GE`j|{': 4, 'GHQ\\z{': 4, 'GSDj}{': 4, 'GcO|z{': 4, 'GP`Z~{': 4, 'G@jR~o': 4, 'GHE}^s': 4, 'G@jR~s': 4, 'GPFJz{': 4, 'GHFLz{': 4, 'GANe|{': 4, 'GPFJ~{': 4, 'GIIZ~o': 4, 'GIH{~s': 4, 'GIIZ~s': 4, 'GIIZz{': 4, 'GIIZ~{': 4, 'GII^~w': 4, 'GII^~{': 4, 'GGdjck': 4, 'GEG|Q[': 5, 'GDXHYk': 5, 'GGt`kk': 5, 'GYCWx[': 4, 'GFGkY[': 4, 'GFPHX[': 4, 'GLPHW{': 4, 'G@Mq]S': 4, 'GG\\_{k': 4, 'G@LuMS': 4, 'G?sxjc': 5, 'G@Mi]c': 5, 'GGXW|c': 5, 'GAK}NC': 5, 'G?Sx~_': 4, 'GGFXps': 4, 'GAK{^C': 4, 'GAXg|c': 4, 'GPXIk{': 5, 'G[CXY{': 4, 'GiCXX{': 4, 'GXPG{{': 4, 'GRPH[{': 4, 'GGXss{': 4, 'GDKmI{': 5, 'GATtP{': 5, 'GGX\\c{': 5, 'GHXKk{': 5, 'G@LuP{': 4, 'GCK~A{': 4, 'GPK]I{': 4, 'GAS~@{': 4, 'GIS\\H{': 4, 'G@Xmc{': 4, 'GiCX\\{': 4, 'GATtT{': 5, 'GPK]J{': 4, 'G@LuR{': 4, 'GAS~D{': 4, 'GIS\\L{': 4, 'G@LuV{': 4, 'GFKjM[': 4, 'G@jPzs': 4, 'G@xPzk': 4, 'GANa|s': 4, 'GBPX|[': 4, 'GHFMX{': 4, 'G@Llms': 4, 'GAK}vK': 5, 'GGT\\tk': 4, 'GIDX|[': 4, 'GXDH}{': 4, 'GAX\\l{': 4, 'GBKnM{': 4, 'GPC}Z{': 4, 'G@W}j{': 4, 'GAL^L{': 4, 'GID\\\\{': 4, 'G@W}n{': 4, 'G@Wx}k': 4, 'GCSxx{': 4, 'GAoxx{': 4, 'G@Wx}{': 4, 'GCKxz{': 4, 'GAKx}{': 4, 'GGKx}{': 4, 'GAKx~{': 4, 'GAM^H{': 4, 'G@Y[y{': 4, 'GCSx~K': 4, 'GASx{{': 4, 'GAcx~[': 4, 'G@dX~[': 4, 'GCSxz{': 4, 'GAM[z{': 4, 'GCSx~{': 4, 'GALX~K': 4, 'G@TX~[': 4, 'GASx|{': 4, 'GASx~{': 4, 'G@\\`}k': 4, 'GAYXx{': 4, 'G@Xi{{': 4, 'GHOx}{': 4, 'G@Wzm{': 4, 'GAKz\\{': 4, 'G@TZ\\{': 4, 'GGTX|{': 4, 'GAKz^{': 4, 'GAMq~S': 4, 'GCoxzk': 4, 'G@hqy{': 4, 'GBI[z[': 4, 'G@fRZ[': 4, 'G@Tq|[': 4, 'GAN`}[': 4, 'G@hYx{': 4, 'G@iiy{': 4, 'GDHY~[': 4, 'GAMq~[': 4, 'GCK}Z{': 4, 'G@hYz{': 4, 'G@eZZ{': 4, 'GAXk|{': 4, 'G@hY~{': 4, 'G@wy~k': 4, 'G@W}}{': 4, 'G@L^n[': 4, 'G@Ll}{': 4, 'G@L^Z{': 4, 'G@S~]{': 4, 'G@S~n[': 4, 'G@W}~{': 4, 'GBcx~[': 4, 'GCKzz{': 4, 'GCKz~{': 4, 'GBSx~[': 4, 'GAK|z{': 4, 'GASz|{': 4, 'GAK~Z{': 4, 'GAKz~{': 4, 'GDTX~[': 4, 'GCK}z{': 4, 'GAS||{': 4, 'GAS|~{': 4, 'GAwx~k': 4, 'GAK|~[': 4, 'G@T^\\{': 4, 'GGK}}{': 4, 'GGK}~{': 4, 'GAK~~w': 4, 'GAK~~{': 4, 'GCxPjK': 4, 'GALfKw': 4, 'GAphlc': 5, 'GCS~FC': 4, 'GAKk~G': 5, 'G@Ej]o': 4, 'G?dX~_': 4, 'GSpah{': 4, 'GiG[X{': 4, 'GcO~@{': 4, 'GAYuP{': 4, 'G_X\\`{': 4, 'GCS~@{': 4, 'GsOgz{': 4, 'GC^DJ{': 4, 'GAM^B{': 4, 'GCS~F{': 4, 'G@ZT]s': 4, 'GANbs{': 4, 'G@fazs': 4, 'G@}QnK': 4, 'GANfK{': 4, 'GANb[{': 4, 'G@d^VK': 4, 'GAMZvK': 4, 'GAMZnS': 4, 'GF`H~[': 4, 'G_dtZ{': 4, 'GAM^J{': 4, 'G@d^J{': 4, 'G@d^f[': 4, 'GAM^N{': 4, 'G@yY~k': 4, 'G@d^^[': 4, 'GCS~n[': 4, 'G@U^Z{': 4, 'GCS~Z{': 4, 'G@d^^{': 4, 'GBS{~[': 4, 'GAMZz{': 4, 'GCS|z{': 4, 'GAMZ~{': 4, 'GCS~~w': 4, 'GCS~~{': 4, 'GDhZvK': 4, 'GGl]lk': 4, 'GBlLnK': 4, 'GChrzw': 4, 'G@Z]p{': 4, 'G@d^^W': 4, 'G@Yu}w': 4, 'GGK}}w': 4, 'GBQ|r[': 4, 'GGMu}w': 4, 'GPXs}{': 4, 'GChzr{': 4, 'G@j]r{': 4, 'GAmrZ{': 4, 'GON]r{': 4, 'GHQ|u{': 4, 'GAY|v{': 4, 'G@nR^c': 4, 'G@ljmk': 4, 'G@y]jk': 4, 'G@jZvc': 4, 'G@jYzs': 4, 'G@ZY|s': 4, 'G@ZU|w': 4, 'G@Mz]s': 4, 'G@x[zk': 4, 'G@hzms': 4, 'G@xY|k': 4, 'G@UznS': 4, 'GCNZnS': 4, 'GHMu]{': 4, 'GWMZm{': 4, 'GCp|r{': 4, 'G@h}r{': 4, 'G@lmj{': 4, 'GCx\\j{': 4, 'GHE~U{': 4, 'G@lmn{': 4, 'GJQZ\\s': 4, 'GA]tj[': 4, 'G@]vI{': 4, 'GIWzk{': 4, 'GBS|^K': 4, 'GAL~fS': 4, 'GFO|Z[': 4, 'GHRZts': 4, 'G@Z[zs': 4, 'GAkzZk': 4, 'GBQ|Zs': 4, 'G@Lz]s': 4, 'G@UvZw': 4, 'GAK~Zw': 4, 'GHPy|s': 4, 'G@Unjw': 4, 'GJPk|{': 4, 'GbOz\\{': 4, 'GAljl{': 4, 'G@\\ml{': 4, 'GG\\\\j{': 4, 'GANjt{': 4, 'GHP}t{': 4, 'GG\\\\n{': 4, 'GGk}mk': 4, 'G@h}vc': 4, 'GOszjk': 4, 'G@jrus': 4, 'G@h^]w': 4, 'GGS}|w': 4, 'GGNU|w': 4, 'G@x]h{': 4, 'GCxXzk': 4, 'G@fZnS': 4, 'GAK|~W': 4, 'G@U~b[': 4, 'G@hy~c': 4, 'GPW}m{': 4, 'GX_y}{': 4, 'GO^Sz{': 4, 'G@zSz{': 4, 'GAk~J{': 4, 'GCL~R{': 4, 'G@Y~e{': 4, 'GAM~V{': 4, 'GqLrS{': 4, 'GBRlts': 4, 'G@Y]~g': 4, 'GBQx~S': 4, 'GGM]~g': 4, 'GII]|w': 4, 'G@S~nW': 4, 'GAM^nW': 4, 'GhTc|{': 4, 'GD`~R{': 4, 'G@fvR{': 4, 'GANvR{': 4, 'GANvV{': 4, 'GANv^o': 4, 'GA|lnk': 4, 'GGs~nk': 4, 'GHQ~u{': 4, 'GAw~n{': 4, 'GAll~k': 4, 'GOdzz{': 4, 'GGU|z{': 4, 'GBQ|~[': 4, 'GGU|~{': 4, 'G@T~^s': 4, 'GAYz~s': 4, 'GGLz}{': 4, 'GGL}~{': 4, 'GAL~n[': 4, 'GANv^{': 4, 'GGU~~{': 4, 'GBMZZ[': 4, 'GC[znK': 4, 'G@X\\|w': 4, 'G@hzuk': 4, 'GCKzzw': 4, 'GALzs{': 4, 'GALl|w': 4, 'GChZzw': 4, 'GHgy}{': 4, 'G@hzu{': 4, 'GCLzr{': 4, 'G@mqz{': 4, 'GAdzt{': 4, 'GOLzu{': 4, 'GCLzv{': 4, 'GBMlY{': 4, 'GBgzY{': 4, 'GBqix{': 4, 'GBMj[{': 4, 'GDLjY{': 4, 'GDS~J[': 4, 'G@h\\zw': 4, 'G@lizk': 4, 'G@U~Js': 4, 'GCS|zw': 4, 'GBTX|[': 4, 'GHW{}{': 4, 'GPWy}{': 4, 'G@Yzu{': 4, 'GDczZ{': 4, 'GAkzj{': 4, 'GAtp|{': 4, 'GGkzm{': 4, 'GAkzn{': 4, 'GC[}nK': 4, 'GDXi{{': 4, 'GDpix{': 4, 'GBYi{{': 4, 'GAN\\vK': 4, 'GBh[~[': 4, 'G@uZn[': 4, 'GA]\\j{': 4, 'GAN\\r{': 4, 'GAN\\v{': 4, 'GFcz^[': 4, 'GDL^^[': 4, 'G@d~^s': 4, 'GAMz~s': 4, 'G@d}~s': 4, 'GCL~v[': 4, 'GBc~^{': 4, 'G@Z\\~s': 4, 'G@Z]|{': 4, 'G@Vlz{': 4, 'G@Vl~{': 4, 'GCL~r{': 4, 'G@fjz{': 4, 'GCLzz{': 4, 'GAM|z{': 4, 'GAdz|{': 4, 'GCLz~[': 4, 'GCLz~{': 4, 'GAL|~s': 4, 'GAMzz{': 4, 'GAMz~{': 4, 'GAN^\\{': 4, 'GAL}|{': 4, 'GAN\\~{': 4, 'GANl~s': 4, 'G@U~n[': 4, 'GAM~Z{': 4, 'GGN]|{': 4, 'GAM~^{': 4, 'GCL~~{': 4, 'G@djzw': 4, 'GIHzs{': 4, 'GILi|{': 4, 'GAXzt{': 4, 'GALzt{': 4, 'GALzv{': 4, 'GFSz^[': 4, 'GBS~^[': 4, 'GBS~^{': 4, 'GBSz~[': 4, 'GALz~{': 4, 'GAL~~{': 4, 'GAN~vs': 4, 'GANn~w': 4, 'GAM~~w': 4, 'GAL~~w': 4, 'GAN~v{': 4, 'GAN~~{': 4, 'G?K~E_': 4, 'G_K|Ac': 5, 'G?X\\d_': 5, 'G`Ko]C': 4, 'G@N@mS': 4, 'GBaHrK': 5, 'G`M@i[': 5, 'GYScG{': 4, 'GIaHpk': 5, 'GWTT?{': 5, 'GHNE?{': 4, 'GWCW}K': 4, 'G@r@pk': 4, 'GDh@i[': 5, 'G``Hpk': 5, 'GDh?zK': 5, 'G`GXuK': 4, 'GJ_MH{': 4, 'GeGaX{': 5, 'GJaAX{': 4, 'GaUd@{': 4, 'G@ouH{': 4, 'GCYRH{': 5, 'G`_qX{': 5, 'Gl?IX{': 4, 'GSOqX{': 5, 'GBYEH{': 5, 'G_KuH{': 4, 'G]?IX{': 4, 'GTPCZ{': 4, 'GGdcj{': 4, 'GB`cZ{': 5, 'GK_ZJ{': 4, 'G]?KZ{': 4, 'G_KuN{': 4, 'G@Ku]W': 4, 'G`G]vG': 3, 'G@NMRk': 4, 'GCdjRk': 4, 'GKb_zs': 3, 'G@r@x{': 3, 'GAi`y{': 5, 'GKEJj[': 4, 'GQOX~K': 4, 'G_Kp}[': 3, 'G`G]vK': 3, 'G@NMVk': 3, 'G@r@z{': 4, 'GCXcz{': 4, 'GoDcz{': 3, 'G@r@~{': 3, 'GAMlQk': 5, 'GCXaxw': 4, 'G_KtYw': 5, 'GHE[r[': 4, 'GCTjTk': 4, 'GPDYr[': 4, 'GKSi\\k': 4, 'GcCxr[': 4, 'GOTPx{': 4, 'GGeQx{': 4, 'GCXax{': 4, 'G_KtY{': 4, 'GKOix{': 4, 'G_Kqx{': 4, 'G`G\\Y{': 4, 'GPDYv[': 4, 'GGePz{': 4, 'GCXa|{': 4, 'GOTPz{': 4, 'GKHI|{': 4, 'G_Ksz{': 4, 'GOTP~{': 4, 'G`G^eW': 4, 'GKW[Zk': 4, 'GKFcZs': 4, 'GKdHZk': 5, 'GQIHy{': 5, 'G``Hx{': 4, 'GK_Zj[': 4, 'GQOZl[': 5, 'G`G^e[': 4, 'G`GX}[': 4, 'G`MI^k': 4, 'G`QHz{': 4, 'GgEcz{': 4, 'GKOkz{': 5, 'G``H~{': 4, 'G_KxuK': 4, 'G`Cxu[': 4, 'G`KpY{': 4, 'G`Kp]{': 3, 'G_Kp}{': 3, 'G`GXz{': 4, 'G`GX~{': 3, 'GGeRzw': 3, 'G@rDzw': 4, 'GOTR|w': 4, 'G`G^]w': 3, 'GGeR~w': 3, 'GGeRz{': 3, 'G@rDz{': 3, 'GOTR|{': 4, 'G`G^]{': 3, 'GGeR~{': 3, 'G`GZzw': 4, 'G`G\\zw': 4, 'G`GZ~w': 4, 'G`GZz{': 4, 'G`G\\z{': 4, 'G`GZ~{': 4, 'G`G^~w': 3, 'G`G^~{': 3, 'GAK^NG': 4, 'GChJjg': 4, 'GII[vC': 4, 'GIC\\\\W': 4, 'GHdJKk': 5, 'GBha[k': 4, 'GKG{Ys': 5, 'GGSs{w': 4, 'GK`XrK': 4, 'GI_y\\c': 4, 'G`C\\ZW': 4, 'GCVf@{': 4, 'GBJMP{': 4, 'GcX_x{': 4, 'GdPcX{': 4, 'GEXcX{': 4, 'GIePX{': 4, 'G`XSX{': 5, 'GKSmH{': 4, 'GcOxp{': 4, 'G@re`{': 4, 'GDJMR{': 4, 'GII[r{': 4, 'GPTSZ{': 4, 'GKFLR{': 4, 'GII[v{': 4, 'G@H}uo': 4, 'GBjMPk': 4, 'G@Q|ro': 4, 'GILc{w': 4, 'G@vTb[': 4, 'GLgZI{': 4, 'GOlra{': 4, 'GUSsZ[': 4, 'GTTSZ[': 4, 'GBr@x{': 4, 'GBYa{{': 4, 'GGmre{': 4, 'GEq`z{': 4, 'GDhaz{': 4, 'GDXcz{': 4, 'GcStZ{': 4, 'GSTTZ{': 4, 'GDha~{': 4, 'GA\\s\\c': 4, 'G@lra[': 4, 'G@drZo': 4, 'GBXksk': 4, 'G@\\vC{': 4, 'GGlrc{': 4, 'GJW]H{': 4, 'GHhqs{': 4, 'GhKq[{': 4, 'GBZ@x{': 4, 'GJW]L{': 4, 'GBZ@|{': 4, 'GDXa|{': 4, 'GBZ@z{': 4, 'GLHI|{': 4, 'GgKq|{': 4, 'GBZ@~{': 4, 'GIS{tK': 4, 'G@X\\tg': 4, 'G@p^Lo': 4, 'GQM]b[': 4, 'GUSkj[': 4, 'GPhqq{': 4, 'GLMJI{': 4, 'GDNMb[': 4, 'GTS]J[': 4, 'GBYe[{': 4, 'GIMa{{': 4, 'GRIIy{': 4, 'GBYU\\[': 4, 'GRO\\][': 4, 'GIMQ|[': 4, 'GRDI|[': 4, 'GHerU{': 4, 'Gae`z{': 4, 'GactZ{': 4, 'GLHKz{': 4, 'GPdaz{': 4, 'GEotZ{': 4, 'GUO\\Z{': 4, 'GPda~{': 4, 'GPLYuK': 4, 'GRTP[[': 4, 'G@NNMo': 4, 'GYE[r[': 4, 'GLQ[r[': 4, 'GpKqY{': 4, 'GLFKr[': 4, 'GhKsY{': 4, 'GBrDX{': 4, 'GWTP{{': 4, 'GoTPx{': 4, 'GPTP}[': 4, 'GpKq]{': 4, 'GgePz{': 4, 'GIeTZ{': 4, 'GgKsz{': 4, 'GMELZ{': 4, 'GoKqz{': 4, 'GoKq~{': 4, 'G@lre[': 4, 'GDh`y{': 4, 'GDX`y{': 4, 'GQOxx{': 4, 'GKQXx{': 5, 'GK`Xx{': 4, 'GDX`}{': 4, 'GSOxz{': 4, 'GQOxz{': 4, 'GKHY|{': 4, 'G`HY|{': 4, 'GQOx~{': 4, 'GHd[vK': 5, 'GQUJh{': 5, 'GHeIzk': 5, 'GQSjk{': 5, 'GBbJ\\s': 5, 'GKI]Zs': 5, 'GQMJi{': 5, 'GIMJk{': 5, 'GQIZq{': 5, 'GB`m\\s': 5, 'GKQkzs': 5, 'GaIXx{': 5, 'GoDix{': 5, 'GKdP~[': 5, 'Gacp~[': 5, 'GQ`Xz{': 5, 'GH`[z{': 5, 'GQH[z{': 5, 'GWFKz{': 5, 'G`FLZ{': 5, 'GH`[~{': 5, 'GIM[vK': 4, 'GHeQz[': 4, 'GQQZp{': 4, 'GKEmZs': 4, 'GQOzs{': 4, 'GK`ix{': 5, 'GIeP~[': 4, 'GK`Xz{': 4, 'GQO{z{': 4, 'GKFLZ{': 4, 'GK`X~{': 4, 'GDjBzw': 4, 'GBZD~w': 4, 'GDjBz{': 4, 'GBZD~{': 4, 'GDhb}w': 4, 'GIax~s': 4, 'GDhb}{': 4, 'GSOzz{': 4, 'GQO|z{': 4, 'GSOz~{': 4, 'GBZB|w': 4, 'GI`x~s': 4, 'GBZB|{': 4, 'GI_zz{': 4, 'GI_z~{': 4, 'GBdd~W': 4, 'GHay~s': 4, 'GBdd~[': 4, 'GKO}|{': 4, 'GH`\\z{': 4, 'GPQZz{': 4, 'GB`m|{': 4, 'GQDm|{': 4, 'GPQZ~{': 4, 'G`H\\~o': 4, 'G`Iy~s': 4, 'G`H\\~s': 4, 'GK_}z{': 4, 'G`H\\z{': 4, 'G`IZz{': 4, 'G`IZ~{': 4, 'GI_~~w': 4, 'GI_~~{': 4, 'GGdq\\c': 5, 'GH`ZKs': 5, 'GK`XjS': 5, 'GcKhYk': 5, 'GEopZK': 5, 'GIG{[s': 5, 'GIK]LK': 5, 'GHdak[': 5, 'GKC\\ZW': 5, 'G`G{Ys': 5, 'GQG{Ys': 5, 'GGS{sk': 5, 'GDReP{': 5, 'GEWmH{': 5, 'GBYMH{': 5, 'GcWih{': 5, 'GcUbH{': 5, 'GdQaX{': 5, 'GKW]H{': 5, 'G`W]H{': 5, 'GKXSX{': 5, 'G`qah{': 5, 'GKdPX{': 5, 'GcSpX{': 5, 'GDRLR{': 5, 'GKJKr{': 5, 'GQSsZ{': 5, 'GIMSZ{': 5, 'GIMS^{': 5, 'GEgZJK': 4, 'GqG^?{': 5, 'GKhQh[': 4, 'GqGgw{': 4, 'GdGgy[': 4, 'GEhPZK': 5, 'GHpHkk': 5, 'GUGgy[': 4, 'GcKgzK': 5, 'GK_ZjW': 4, 'GWC[yw': 4, 'G@pq\\c': 4, 'GDZEH{': 4, 'GUHIX{': 4, 'G`UeH{': 5, 'GdHIX{': 4, 'GLPKX{': 4, 'GSXQX{': 5, 'GkCXX{': 4, 'GDXMH{': 5, 'G`JUP{': 4, 'GWEYp{': 4, 'GLQKZ{': 4, 'GoDXr{': 4, 'GIiSZ{': 5, 'GYC[Z{': 4, 'GWEYv{': 4, 'GQSxuK': 4, 'G`qihs': 5, 'GPTZc[': 4, 'GQSzc[': 5, 'G`K|a[': 4, 'GQLXuK': 5, 'GHe]b[': 4, 'GhK\\I{': 4, 'GLUKj[': 5, 'GpKZI{': 4, 'G]C[Z[': 4, 'GQV@x{': 4, 'GQT`{{': 4, 'GpKZM{': 4, 'GMaHz{': 4, 'G`Maz{': 4, 'GKUTZ{': 5, 'G`Lcz{': 4, 'GkC\\Z{': 4, 'G`Ma~{': 4, 'GILksk': 5, 'G@h\\rg': 5, 'G@L}eS': 5, 'G@p^Tg': 5, 'GQU\\b[': 5, 'GTTKj[': 5, 'GLcjI{': 5, 'GPlRI{': 5, 'GDVLb[': 5, 'GUS\\J[': 5, 'G`Su\\[': 5, 'GQMay{': 5, 'GJII{{': 5, 'GBou\\[': 5, 'GJEM\\[': 5, 'GHeje{': 5, 'Ge_hz{': 5, 'GQUTZ{': 5, 'GTHIz{': 5, 'GHdcz{': 5, 'GEUdZ{': 5, 'GeClZ{': 5, 'GTHI~{': 5, 'G?lrjo': 4, 'GRTHk[': 5, 'G`Kza[': 4, 'G@lrIs': 5, 'GA\\stK': 5, 'GDXjc{': 4, 'GhKZK{': 4, 'GHlRK{': 5, 'GJLMH{': 4, 'GHL^C{': 4, 'GQT`x{': 4, 'GJLML{': 4, 'GQT`|{': 4, 'G`La|{': 4, 'GHda|{': 5, 'GJQHz{': 4, 'GHNA|{': 4, 'GJQH~{': 4, 'GAL}dS': 5, 'G@rLrg': 4, 'GQ]Sj[': 4, 'GtOWz[': 4, 'GD^Cj[': 5, 'GPL^A{': 4, 'GHM^A{': 4, 'GLPL[{': 4, 'GIU`{{': 4, 'GPNAy{': 4, 'GHM^E{': 4, 'Gcd`z{': 4, 'GqC\\Z{': 4, 'GEddZ{': 5, 'GHNCz{': 4, 'GPNAz{': 4, 'GPNA~{': 4, 'G`Kze[': 4, 'G`M`y{': 4, 'GQSq|[': 5, 'G`L`y{': 4, 'GYCY|[': 4, 'G`Oxx{': 4, 'GgEXx{': 4, 'G`L`}{': 4, 'G`_xz{': 4, 'GQHY|{': 5, 'G`Oxz{': 4, 'GWDY|{': 4, 'G`Ox~{': 4, 'G[SW~K': 4, 'GoCyzs': 4, 'GBamZs': 5, 'GWEZq{': 4, 'GWDZs{': 4, 'GkCX~[': 4, 'GoDXz{': 4, 'GIakz{': 5, 'GWD[z{': 4, 'GWEY~{': 4, 'GJQL|w': 4, 'GJQL~w': 4, 'GJQL|{': 4, 'GJQL~{': 4, 'G`Ld}w': 4, 'G`Qx~s': 4, 'G`Ld}{': 4, 'G`_zz{': 4, 'G`O|z{': 4, 'G`_z~{': 4, 'GDdb~W': 5, 'GPQy~s': 5, 'GDdb~[': 5, 'GcG}z{': 5, 'GHaZz{': 5, 'GPP\\z{': 5, 'GEHm|{': 5, 'GKDm|{': 5, 'GOUr~{': 5, 'GJQJ|w': 4, 'G`Px~s': 4, 'GJQJ|{': 4, 'G`Ozz{': 4, 'G`Oz~{': 4, 'G@nB~g': 4, 'GWEy~s': 4, 'G@nB~k': 4, 'GgC}|{': 4, 'GWD\\z{': 4, 'GWEZz{': 4, 'G@qr~{': 4, 'G`O~~w': 4, 'G`O~~{': 4, 'G`O|Uc': 5, 'G@prKs': 5, 'G@pilc': 5, 'GI`hks': 5, 'GEGlYw': 5, 'GBIkYs': 5, 'GBKk]K': 5, 'GGxPkk': 5, 'G@IyuS': 5, 'GAIkzo': 5, 'GGppks': 5, 'GAKl]g': 5, 'GALelW': 5, 'G?S}tg': 5, 'GQQuP{': 5, 'GQqah{': 5, 'GgK]H{': 5, 'GgW[h{': 5, 'GIUcX{': 5, 'GcorH{': 5, 'GA]eH{': 5, 'GAYm`{': 5, 'G_W}`{': 5, 'GcQrP{': 5, 'GCsrH{': 5, 'GCUrP{': 5, 'GSXKj{': 5, 'GCZLb{': 5, 'GA]TJ{': 5, 'GANTR{': 5, 'GANTV{': 5, 'GrMAG[': 5, 'G[O]`[': 4, 'GDpPZK': 4, 'GHp_{k': 4, 'GII]dS': 4, 'GKhPi[': 4, 'GKgYjK': 5, 'GQO|eS': 5, 'GHoikk': 4, 'GRG[Y[': 4, 'GAg~Ec': 5, 'GGpo|c': 4, 'GAKmnG': 5, 'GIG\\[w': 4, 'GChRjW': 5, 'GQKg}K': 5, 'GI`g|c': 5, 'G`G\\Yw': 4, 'GAhilc': 4, 'GQGZ[w': 5, 'GB`i\\c': 5, 'GAK\\^G': 5, 'GGEY|o': 4, 'G_C|Zo': 5, 'GAEj\\o': 5, 'GR`MH{': 4, 'GDpeH{': 4, 'GkHGx{': 4, 'GbHKX{': 4, 'Gd`aX{': 4, 'GMHKX{': 4, 'GdOmH{': 4, 'GEXLH{': 4, 'GBQmP{': 4, 'G_Yu`{': 4, 'GcXHh{': 4, 'GKTLH{': 4, 'G`XKh{': 5, 'G`Qm`{': 5, 'GKLMH{': 4, 'GMEHX{': 4, 'GCX^@{': 4, 'G_cz`{': 4, 'G@VeP{': 5, 'GKS\\H{': 4, 'GC\\eH{': 4, 'G[O[Z{': 4, 'GDZCZ{': 4, 'GKNCZ{': 4, 'GQK]J{': 4, 'GGU\\b{': 4, 'GGnCj{': 4, 'GRDKZ{': 4, 'GGd\\f{': 4, 'GAL|eS': 4, 'GIL[tK': 4, 'G@MzeS': 4, 'G@h]^_': 4, 'GBq\\b[': 4, 'GRUKj[': 4, 'G\\CiY{': 4, 'GXcZI{': 4, 'GFULJ[': 4, 'GVO[Z[': 4, 'GBgu][': 4, 'GBV@|[': 4, 'GIUP|[': 4, 'G@l`}k': 4, 'GWMZe{': 4, 'GDqRZ{': 4, 'GSURZ{': 4, 'GBguZ{': 4, 'GPLUZ{': 4, 'GEcnJ{': 4, 'GQc^J{': 4, 'GDLe^{': 4, 'GRKim[': 4, 'G@iZrk': 4, 'G@X\\rk': 4, 'GGTs|s': 4, 'GAZP|s': 4, 'GBHY|[': 4, 'G@hszs': 4, 'GPLJi{': 5, 'GGLZk{': 4, 'GJCl]{': 4, 'GAZP|{': 4, 'GPLR]{': 4, 'GOMqz{': 4, 'G@Yqz{': 4, 'GANR\\{': 4, 'GIEZ\\{': 4, 'G@Yq~{': 4, 'GD]Q^K': 4, 'GAejrk': 5, 'GANRt[': 5, 'GA]Rl[': 4, 'G@hu]s': 4, 'GGNa{{': 4, 'GANel[': 4, 'GCNPz[': 5, 'GEcjn[': 4, 'G_f`z{': 4, 'GAdtZ{': 4, 'GANTZ{': 4, 'GANT^{': 4, 'GBQm\\s': 4, 'GKsXnK': 4, 'GPFJq{': 4, 'GIEjs{': 4, 'G@jUZs': 4, 'GREIz[': 4, 'GBRL\\s': 4, 'GHFJ[{': 4, 'GcDjX{': 4, 'GPDZu[': 4, 'GIEZt[': 5, 'G@p^Tk': 5, 'GQEZr[': 4, 'GGU\\h{': 4, 'GdDH~[': 4, 'GE`lZ{': 4, 'GQcZn[': 4, 'GPD]Z{': 4, 'GGU\\j{': 4, 'GAfdZ{': 4, 'GOdqz{': 4, 'GGU\\n{': 4, 'GBkrM[': 4, 'GHUQ|[': 4, 'GO\\Pzk': 4, 'GDhPz[': 4, 'GBYQ|[': 4, 'GRDH}[': 4, 'GH`Yx{': 4, 'GKIYx{': 5, 'GH`i{{': 5, 'GLHH}{': 4, 'GBMb]{': 4, 'GI`X|{': 4, 'GOSzj{': 4, 'GDO|Z{': 4, 'GCXZl{': 4, 'G_LZl{': 4, 'GOSzn{': 4, 'GBgze[': 5, 'GQSp}[': 5, 'GDd`z[': 5, 'GDXHzk': 5, 'GBNA|[': 5, 'GJEI|[': 5, 'GPSq}[': 5, 'G@Yszs': 5, 'GQHYx{': 5, 'GHd`}{': 5, 'GDLb]{': 5, 'GaHX|{': 5, 'GOUpz{': 5, 'GPOyz{': 5, 'GEHZ\\{': 5, 'GKDZ\\{': 5, 'GPOy~{': 5, 'GAmZfK': 5, 'GBai~S': 5, 'GBaizs': 5, 'GAu`zk': 5, 'GA]bk{': 5, 'G@pt]s': 5, 'GB_}^S': 5, 'GBUJl[': 5, 'GANR\\s': 5, 'GWDi{{': 5, 'GWEiy{': 5, 'GEd`~[': 5, 'GCsrn[': 5, 'GoFHz{': 5, 'GB`\\Z{': 5, 'G@p\\j{': 5, 'GAhsz{': 5, 'G_Ncz{': 5, 'GAiZn{': 5, 'GIk[nK': 4, 'GK_}Zs': 4, 'GQFJp{': 4, 'GGeqzs': 4, 'G@rTZs': 4, 'GQDjs{': 4, 'GKaizs': 4, 'GQCzu[': 4, 'GGUZls': 4, 'G@p^Ls': 4, 'G`DlY{': 4, 'GKFJX{': 5, 'G_Ndi{': 5, 'G`Dj[{': 4, 'GMEH~[': 4, 'GSSZn[': 4, 'GK`\\Z{': 4, 'GQC}Z{': 4, 'GGd\\j{': 4, 'GGfTZ{': 4, 'GOTsz{': 4, 'GGd\\n{': 4, 'G@Ypy{': 4, 'GGNSx{': 4, 'GOSxzk': 4, 'GPOxy{': 5, 'GCZPx{': 5, 'GGfPx{': 4, 'GCKxz[': 4, 'GCXXx{': 4, 'GAhXx{': 5, 'GGdXx{': 4, 'GAK|][': 4, 'G@gzm{': 4, 'GPOx}{': 4, 'GOKyz{': 4, 'GAgxz{': 4, 'GAgx}{': 4, 'GGcx}{': 4, 'GCKz^{': 4, 'GBMI~K': 4, 'GCS|j[': 4, 'GCL\\j[': 4, 'GCNbY{': 4, 'GB`Xz[': 4, 'GCX\\h{': 5, 'G_MrY{': 4, 'G@qYx{': 5, 'GAdp~[': 4, 'GB`X~[': 4, 'GCXXz{': 4, 'GAiXz{': 4, 'G_Li|{': 4, 'GCXX~{': 4, 'G@NQ~S': 5, 'GATp|[': 5, 'G@NSz[': 5, 'GANP~S': 5, 'GALq|[': 5, 'GGNR[{': 5, 'GCYZh{': 5, 'GAhqx{': 5, 'GEIXz[': 5, 'GGfRX{': 5, 'G@pXx{': 5, 'G@NQ~[': 5, 'GANP~[': 5, 'GEHX~[': 5, 'GCczZ{': 5, 'G@pXz{': 5, 'G@c}Z{': 5, 'GGX[|{': 5, 'G@pX~{': 5, 'GGS{~c': 4, 'GHEY~S': 4, 'GGdX|k': 4, 'GGdqx{': 5, 'GGfax{': 5, 'GAMj[{': 4, 'GGXX{{': 5, 'GHD[~[': 4, 'GKDX~[': 4, 'GOcyz{': 4, 'GGS{z{': 4, 'G@X]\\{': 4, 'GGS{~{': 4, 'G@h]^c': 4, 'G@p\\^c': 4, 'G_drX{': 4, 'GALt][': 4, 'G_Lr[{': 4, 'GGduX{': 5, 'G@Mi}[': 5, 'GAMm^k': 4, 'G_Mi~k': 4, 'GCTlZ{': 4, 'G@UmZ{': 4, 'G@h]^{': 4, 'G@hu~o': 4, 'GONq~s': 4, 'GDHm}{': 4, 'G@hu~s': 4, 'GPDZ~[': 4, 'GDHm~{': 4, 'GCZp~s': 4, 'GKG}}{': 4, 'GOS~j{': 4, 'GPO}~{': 4, 'GO[y~k': 4, 'GOLZz{': 4, 'GOLZ~{': 4, 'GA]h~k': 4, 'GHEZ~[': 4, 'GDOz~[': 4, 'GCLlz{': 4, 'GAgzz{': 4, 'GAgz~{': 4, 'G@nI~k': 4, 'GCLnm{': 4, 'GCW}~k': 4, 'GCW}z{': 4, 'G@pZ|{': 4, 'G@qZz{': 4, 'G@qZ~{': 4, 'GGl[~k': 4, 'G_S|~k': 4, 'GKC}~[': 4, 'GOSz}{': 4, 'GGUZ|{': 4, 'G@p^\\{': 4, 'GOUZz{': 4, 'GOUZ~{': 4, 'GCLn~w': 4, 'GCLn~{': 4, 'GGdrc[': 4, 'GcGxq[': 5, 'GgCXxw': 4, 'GKX_w{': 4, 'G`KsY[': 4, 'G_Spxw': 5, 'GI`ps[': 5, 'GCXgzc': 4, 'G_Cxzo': 4, 'G_K{Zc': 4, 'GDPjS{': 5, 'GWDYp{': 4, 'GLPH[{': 4, 'GoCxq{': 4, 'GKX_{{': 4, 'GQTPX{': 5, 'GKXHk{': 5, 'GcGxq{': 5, 'GQSZH{': 4, 'G`KqX{': 4, 'GCXjc{': 4, 'G_K|a{': 4, 'GWDYt{': 4, 'GQTP\\{': 5, 'G`KqZ{': 4, 'GQSZL{': 4, 'G`KsZ{': 4, 'G`Kq^{': 4, 'G}GOW[': 4, 'GwC]`[': 4, 'GKdPZK': 5, 'GJ`_{[': 5, 'G`O|eS': 4, 'GJG[[[': 5, 'GClRJK': 5, 'G@[uMK': 4, 'G_K~Ec': 4, 'GQG\\Yw': 6, 'GI`p[s': 5, 'G`Kg}K': 4, 'GGdrKs': 5, 'GAElZo': 5, 'GGE[zo': 4, 'G_Kx]c': 4, 'GTPMH{': 4, 'GeGiX{': 5, 'GJQKX{': 4, 'GcdbH{': 4, 'G`ouH{': 4, 'GKXKh{': 5, 'G`LMH{': 5, 'G`QuP{': 4, 'GKcZH{': 5, 'GCXm`{': 5, 'G_sph{': 4, 'G@^EH{': 4, 'GTPKZ{': 4, 'GKYKj{': 4, 'GQS\\J{': 5, 'GG]Sj{': 4, 'GGySj{': 4, 'GGeZf{': 4, 'G`r@xw': 3, 'GQLYtK': 5, 'G`KxuK': 3, 'G@NM^_': 3, 'GJa[r[': 4, 'GwCxq{': 4, 'GNEKZ[': 3, 'G`Ku][': 3, 'GQTP|[': 5, 'G`Kp}[': 3, 'GwCxu{': 3, 'GKeRZ{': 4, 'G`KuZ{': 4, 'GKc^J{': 3, 'G`Ku^{': 3, 'GPTQ|[': 4, 'GbGxu[': 4, 'G`HXzs': 4, 'G`IXzs': 4, 'GQPXx{': 4, 'G`FJX{': 5, 'G`IYx{': 4, 'G_Kzrk': 4, 'G_K|rk': 4, 'GgKp}{': 4, 'GQPX|{': 4, 'G`Kr]{': 4, 'G`Gyz{': 4, 'GQDZ\\{': 4, 'G`G{z{': 4, 'G`Gy~{': 4, 'GK`kzs': 4, 'GK[[nK': 4, 'GQEjq{': 5, 'GJEJ[{': 4, 'G@quZs': 4, 'GKaZZs': 4, 'GKDj[{': 4, 'G_Neh{': 4, 'GQDZt[': 5, 'GGeZrk': 4, 'G@rLrk': 4, 'GeCh~[': 4, 'GK`kz{': 4, 'GKcZn[': 4, 'GQD\\Z{': 5, 'GGdsz{': 4, 'GGfcz{': 4, 'GGeZn{': 4, 'GQKY~K': 4, 'GOLYzk': 4, 'GGM[zk': 4, 'GCNRZ[': 4, 'G_cxzk': 4, 'GQSX~K': 4, 'GOTXzk': 4, 'GKEXz[': 5, 'G_N`y{': 5, 'G_L\\h{': 4, 'GOTXx{': 4, 'GCXix{': 4, 'GAMlY{': 5, 'GGS{{{': 4, 'G_K|Y{': 4, 'GPDY~[': 4, 'GQDX~[': 4, 'GOTXz{': 4, 'GGeXz{': 4, 'GCXi|{': 4, 'G_cxz{': 4, 'GOTX~{': 4, 'G`Gxy{': 4, 'G_NPx{': 4, 'G_Sxx{': 4, 'G_Kx}[': 3, 'G`Gx}{': 3, 'G_Kxz{': 4, 'G_Kx}{': 3, 'G_Kx~{': 3, 'G@NM^c': 3, 'G@Lu][': 4, 'G@rH~c': 3, 'G_Lp}[': 4, 'GGdr[{': 4, 'G@K}][': 3, 'G@NM^k': 3, 'G_K}^k': 3, 'GCXkz{': 4, 'G@NMZ{': 4, 'G@NM^{': 3, 'G_K~vg': 3, 'G_Np~s': 3, 'G`G}}{': 3, 'G_K~vk': 3, 'G`Gz}{': 4, 'G`G}~{': 3, 'G_[x~k': 4, 'G_Kzz{': 4, 'G_K|z{': 4, 'G_Kz~{': 4, 'GG][~k': 3, 'G_K}~k': 3, 'GOTZ|{': 4, 'GGeZz{': 3, 'G@rLz{': 3, 'GGeZ~{': 3, 'G_K~~w': 3, 'G_K~~{': 3, 'G]MAG[': 4, 'GQO{vC': 4, 'GB`jKs': 4, 'GGdilc': 5, 'G@o~Ec': 4, 'GBW]LK': 4, 'GBHk[s': 5, 'GBdbK[': 4, 'GEKh]K': 4, 'GAIlqw': 5, 'GCdrRK': 5, 'G@G}]o': 4, 'G@LNMg': 5, 'G?K}ug': 4, 'GSPuP{': 4, 'GEqbH{': 4, 'GIMMH{': 4, 'GaWkh{': 5, 'GsOqX{': 4, 'G_[uH{': 4, 'GAUn@{': 5, 'G_qr`{': 4, 'GAUtP{': 5, 'GEopX{': 4, 'GSLMJ{': 4, 'GCZcr{': 4, 'GBYSZ{': 4, 'G@NUR{': 5, 'G@NUV{': 4, 'GAS|vG': 4, 'G@K~eW': 3, 'GBySj[': 3, 'GrC[Z[': 3, 'GFYKj[': 4, 'GXK]I{': 4, 'GFGm][': 3, 'GXK]M{': 3, 'GFaJZ{': 3, 'GsCZZ{': 3, 'GBeNJ{': 4, 'GFGmZ{': 4, 'GFGm^{': 3, 'G@NNMs': 4, 'GB]S^K': 4, 'GBaZZs': 4, 'GAUrt[': 5, 'G@Ne]s': 4, 'GCdrZ[': 4, 'G@NR][': 5, 'G@Nem[': 4, 'GAS|l[': 5, 'G@NUX{': 4, 'GBeJn[': 4, 'GCfbZ{': 4, 'GCdrZ{': 4, 'G@NUZ{': 5, 'G@NU^{': 4, 'GAS|vK': 4, 'GNGg}[': 4, 'GATltk': 5, 'G@LZvK': 4, 'G@Ltu[': 4, 'GAV`|s': 4, 'G@LY~K': 4, 'G@MY~K': 4, 'G@NJrk': 4, 'G@NLrk': 4, 'G@Kzm[': 4, 'GHK^M{': 4, 'GAS~L{': 4, 'GXCZ]{': 4, 'GATt\\{': 5, 'G@LuZ{': 4, 'G@MuZ{': 4, 'G@Lu^{': 4, 'GC]ZfK': 4, 'GB`k~S': 4, 'GBYJk{': 4, 'GAmazk': 5, 'G@r`}s': 4, 'GBaZ^S': 4, 'GAUjls': 5, 'GB`j[{': 4, 'GWFIx{': 5, 'G_Mrm[': 4, 'GEop~[': 4, 'GC]Rn[': 4, 'GoDkz{': 4, 'GB`kz{': 4, 'GAh\\j{': 5, 'G_MuZ{': 4, 'GCYZn{': 4, 'GBK~E[': 4, 'GYCX}[': 4, 'GBUa|[': 5, 'G@^@zk': 4, 'G@n@zk': 4, 'GXCY}[': 4, 'GWDYx{': 4, 'GWEYx{': 4, 'GHN@}{': 4, 'GFGj]{': 4, 'GgDX|{': 4, 'GAhZl{': 5, 'G@ozj{': 4, 'G@qpz{': 4, 'G@ozn{': 4, 'G@K~e[': 3, 'G@N`}s': 3, 'GEJHx{': 4, 'G@oxzk': 4, 'G@Kx}[': 3, 'G@K~M{': 3, 'GWCx}{': 3, 'G@ox}{': 4, 'G@K}Z{': 4, 'G@K}^{': 3, 'G@NNvg': 3, 'G@Nu^s': 3, 'G@Ne}{': 3, 'G@NNvk': 3, 'G@Ne~{': 3, 'G@rp~s': 3, 'GWC}}{': 3, 'GWC}~{': 3, 'G@vH~k': 4, 'GCdnj{': 4, 'GEG}~[': 4, 'GCYZz{': 4, 'G@o}z{': 5, 'G@NN]{': 4, 'GCYZ~{': 4, 'G@[}^k': 4, 'G@NNj{': 4, 'G@o~j{': 4, 'G@NJz{': 4, 'G@NLz{': 4, 'G@NJ~{': 4, 'G@NN~w': 3, 'G@NN~{': 3, 'G?\\~f_': 3, 'GSlra[': 4, 'GB^fC{': 3, 'GJr@x{': 3, 'GSOzzw': 4, 'G`_zzw': 4, 'GH_}}w': 4, 'GKaZzw': 3, 'GWC}}w': 3, 'GJr@|{': 3, 'GK`zr{': 3, 'GQQ|r{': 4, 'G`Q|r{': 3, 'GK`zv{': 3, 'GK`~vo': 3, 'GK`z~o': 3, 'GKbzvs': 3, 'GK`~vs': 3, 'GK`~v{': 3, 'GK`~r{': 3, 'GK`zz{': 3, 'GK`z~{': 3, 'GK`~~{': 3, 'GIL|eS': 4, 'GQ\\vC{': 4, 'GSP|rs': 4, 'GBbjrs': 4, 'GDRlrs': 4, 'G`J\\rs': 4, 'GI`|ts': 4, 'GQQxzs': 4, 'GIaZ|w': 5, 'GK`Z|w': 4, 'GOS~jw': 4, 'G`Gz}w': 4, 'GCYZ~g': 4, 'GGc}~g': 4, 'GbZ@|{': 4, 'GJZC|{': 4, 'GSQzr{': 4, 'GI`|r{': 4, 'GPQ}r{': 4, 'G`I}r{': 4, 'GI`|v{': 4, 'GJYa{{': 4, 'G_]pzk': 4, 'GB`jzw': 4, 'GOUrzw': 5, 'G_Mrzw': 4, 'GCLjzw': 4, 'G_Kzzw': 4, 'GCXzs{': 4, 'GOTzs{': 4, 'GIpp|{': 4, 'GI`zt{': 4, 'GCXzr{': 4, 'GCXzt{': 4, 'G_Lzt{': 4, 'GCXzv{': 4, 'GDX\\vK': 4, 'GD\\LnK': 4, 'GClrj[': 4, 'GBUtZ[': 4, 'GA^Tl[': 4, 'GG]]lk': 4, 'GDlJnK': 4, 'GGm]jk': 4, 'GOUzjs': 4, 'GDQzZs': 5, 'GCZR|w': 5, 'GGfR|w': 4, 'GAMlzw': 4, 'GCXy|s': 4, 'GO\\Y|k': 4, 'G@rXzs': 5, 'GGT{|s': 4, 'G@p^\\w': 4, 'GHYs}{': 4, 'GPYq}{': 4, 'GPQzu{': 4, 'GCljj{': 4, 'GAmjj{': 4, 'G@r\\r{': 4, 'GOV\\r{': 4, 'GAizv{': 4, 'G`H|us': 4, 'G_kzjk': 4, 'G_Mzjs': 4, 'GGdu|w': 5, 'GO\\X}k': 4, 'G_K|zw': 4, 'G@NN]w': 4, 'GpGy}{': 4, 'G`Izu{': 4, 'G_kzj{': 4, 'GGusz{': 4, 'G_Mzv{': 4, 'GB`~^o': 4, 'GC|jnk': 4, 'G_[~nk': 4, 'GI`~t{': 4, 'G_[~n{': 4, 'GIa~r{': 4, 'GI`||{': 4, 'GI`|~{': 4, 'GC\\j~k': 4, 'GI`z|{': 4, 'G_Lzz{': 4, 'GOUzz{': 4, 'G_Mzz{': 4, 'G_Lz~{': 4, 'GClj~k': 4, 'GC\\l~k': 4, 'GDQz~[': 4, 'GGezz{': 4, 'GCX}|{': 4, 'GOUz~{': 4, 'G_L|~s': 4, 'G`Iz}{': 4, 'G_N\\z{': 4, 'G_Mz~{': 4, 'G_L~~{': 4, 'GR\\eK{': 3, 'G``|rs': 3, 'G@rrrs': 3, 'G@rtrs': 3, 'G`P|ts': 3, 'GH`]|w': 4, 'G`Qxzs': 4, 'GWE]zw': 4, 'GDOz~W': 4, 'GCW}~g': 4, 'GGeZ~g': 3, 'G@o~jw': 4, 'GjQH|{': 3, 'GYTc|{': 3, 'G`azr{': 3, 'GOU~b{': 4, 'GGd~b{': 3, 'G@q~b{': 3, 'GGd~f{': 3, 'GJRH|s': 3, 'GG\\rk{': 3, 'G@]rm[': 4, 'GDQjzw': 4, 'GGdrzw': 4, 'G@qrzw': 4, 'GAgzzw': 4, 'G@qZzw': 4, 'GG\\s{{': 3, 'G@Lzu[': 4, 'GJO}\\{': 3, 'G`Pzt{': 3, 'GAhzt{': 4, 'GG\\sz{': 3, 'G@\\u\\{': 3, 'GG\\s~{': 3, 'G@lu^c': 4, 'G@nJnc': 4, 'G@lrm[': 4, 'GCXu|w': 4, 'G@qzjs': 4, 'G@pZ|w': 4, 'G@rLzw': 4, 'G@Mzu[': 4, 'GHM^M{': 4, 'GWEzu{': 4, 'GCZ\\r{': 4, 'G@luZ{': 4, 'G@lu^{': 4, 'GGd~no': 3, 'GG|s~k': 3, 'GG]^nk': 3, 'G`P~t{': 3, 'GG]^n{': 3, 'G`Q~r{': 3, 'G`Q|z{': 3, 'GGd~n{': 3, 'GG]Z~k': 3, 'GGdz~k': 3, 'GGdzz{': 3, 'G@qzz{': 3, 'GGdz~{': 3, 'G@^L~k': 3, 'G@qz~k': 3, 'G@qz~{': 3, 'GGd~~{': 3, 'G@r~vs': 3, 'G_Nv~w': 3, 'G_L~~w': 4, 'GGd~~w': 3, 'G_N~v{': 3, 'G_N~~{': 3, 'G@?}UO': 4, 'GBAKZO': 5, 'G`AIXo': 5, 'G@NE?{': 4, 'GWC]?{': 4, 'GGeR?{': 4, 'GIMCG{': 5, 'G@NE@{': 3, 'GAUd@{': 4, 'G`MAH{': 4, 'G`G]@{': 4, 'G@NEB{': 3, 'GIMCJ{': 4, 'Gr?G^{': 3, 'GGMSi[': 5, 'GW_Wyk': 5, 'G@hTQk': 6, 'GAYSh[': 5, 'GJWSK[': 5, 'GPPGw{': 5, 'GBOk[[': 5, 'G_gpi{': 5, 'G@UdI{': 5, 'GIcbK{': 5, 'GAdbH{': 5, 'GOopi{': 5, 'GIaGx{': 5, 'G`_pY{': 5, 'GaGgx{': 5, 'Gg_Wx{': 5, 'GOStI{': 6, 'GDHIX{': 5, 'GBaIX{': 5, 'GGdah{': 5, 'G@otI{': 5, 'GJ_JK{': 5, 'GEGiX{': 5, 'GAdbL{': 5, 'GcGgz{': 5, 'GBIKZ{': 5, 'GGdal{': 5, 'GDPHZ{': 5, 'GEGkZ{': 5, 'GDPH^{': 5, 'GWOWw{': 5, 'GoCWz[': 4, 'G@opm[': 4, 'GEGhY{': 4, 'GgCWx{': 4, 'GWCWx{': 3, 'GEGh]{': 4, 'GoCWz{': 3, 'GWCWz{': 3, 'GWCW~{': 3, 'G@iiac': 5, 'GJYCG{': 4, 'GwCZ?{': 4, 'G`J@o{': 4, 'GCd`rK': 5, 'G@N@uK': 4, 'GGW[kk': 4, 'G@K]MK': 4, 'G`NE@{': 3, 'GTPAX{': 4, 'G`LEH{': 4, 'G_oph{': 4, 'GCdbH{': 4, 'G@NEH{': 3, 'GJaCZ{': 3, 'GCdbJ{': 4, 'G@NEJ{': 3, 'G@NEN{': 3, 'GSLIZk': 4, 'GBYKZk': 4, 'GIasZs': 4, 'GDhIZk': 4, 'GIaHx{': 4, 'GoCZj[': 4, 'GcGhy{': 5, 'GBaHz[': 4, 'GWCZm[': 4, 'GEGh}[': 4, 'GBYK^k': 4, 'GSPHz{': 4, 'GIaHz{': 4, 'GQQcz{': 4, 'GPPKz{': 4, 'GSPH~{': 4, 'GpCWz[': 4, 'GDXI\\k': 5, 'GYCWz[': 4, 'G[CWz[': 4, 'GgCXx{': 4, 'GWC[y{': 4, 'GWCYx{': 4, 'GYCW~[': 4, 'GoCXz{': 4, 'GPPI|{': 5, 'GgCXz{': 4, 'GWC[z{': 4, 'GgCX~{': 4, 'G@NFeW': 4, 'G@K}UK': 4, 'GoF_zs': 4, 'GCXkrk': 5, 'GGdkrk': 4, 'GwAWzs': 4, 'GIaJh{': 5, 'GWCY~K': 5, 'G@NFe[': 4, 'G_N@x{': 4, 'GCd`z[': 5, 'Gw?Yx{': 5, 'G@N@}[': 4, 'GJAJ[{': 4, 'G@o}Vk': 4, 'GK`cz{': 4, 'G_N@z{': 5, 'GGYSz{': 4, 'Gw?[z{': 4, 'G_N@~{': 4, 'GaSh\\k': 4, 'G@eZb[': 4, 'GGTktk': 4, 'G@T\\b[': 4, 'GCK}b[': 4, 'GDPJX{': 5, 'GEGlY{': 5, 'GAU`x{': 4, 'GCdax{': 4, 'GGYQx{': 4, 'G@NDY{': 4, 'GEGix{': 5, 'G@T\\f[': 4, 'GaGi|{': 4, 'GCd`z{': 4, 'GGYQ|{': 4, 'GAU`z{': 4, 'G@NCz{': 4, 'GAU`~{': 4, 'GXCW}[': 3, 'G@spm[': 4, 'G@K~A{': 4, 'G@N@x{': 3, 'G@K~E{': 3, 'GWCX}{': 3, 'GEGh}{': 4, 'G@N@z{': 4, 'G@N@~{': 3, 'GoCZzw': 3, 'GWCZ}w': 3, 'GoCZ~w': 3, 'GoCZz{': 3, 'GWCZ}{': 3, 'GoCZ~{': 3, 'GBaNZw': 4, 'GBaJzw': 4, 'G@NF]w': 4, 'GAUb|w': 4, 'GBaJ~w': 4, 'GBaNZ{': 4, 'GBaJz{': 4, 'G@NF]{': 4, 'GAUb|{': 4, 'GBaJ~{': 4, 'G@NBzw': 3, 'G@NDzw': 4, 'G@NB~w': 3, 'G@NBz{': 3, 'G@NDz{': 3, 'G@NB~{': 3, 'G@NF~w': 3, 'G@NF~{': 3, 'G@Kx}{': 3, 'G@Kx~{': 3, 'GEKx~[': 3, 'G@K}}{': 3, 'G@K~]{': 3, 'G@K}z{': 4, 'G@K}~{': 3, 'GHKx}{': 3, 'G@K|z{': 3, 'G@Kz~{': 3, 'G@K~~w': 3, 'G@K~~{': 3, 'GBXk{{': 3, 'GC]ZnK': 3, 'GAS||w': 4, 'G@N]vK': 3, 'GEoxx{': 3, 'GBY[~[': 3, 'GBY[z{': 3, 'G@vP~[': 3, 'G@N]r{': 4, 'G@N]v{': 3, 'G@w}mk': 3, 'G@N^fS': 3, 'GCdznS': 4, 'G@K~]w': 3, 'G@L^nW': 4, 'GXC}]{': 3, 'GCxsz{': 3, 'G@Nmr{': 4, 'G@NvU{': 3, 'G@Nmv{': 3, 'GFox~[': 3, 'GEK~^[': 3, 'GCdz~s': 3, 'GEK~^{': 3, 'GCdzz{': 3, 'G@N]~[': 3, 'G@L}}{': 4, 'G@N]~{': 3, 'G@N^v[': 3, 'G@L~]{': 4, 'G@Nv]{': 3, 'G@Nm~{': 3, 'GBK}~[': 4, 'GEKz~[': 4, 'G@NZz{': 4, 'G@N\\z{': 4, 'G@NZ~{': 4, 'G@N^~{': 3, 'GDYiy{': 4, 'G@s~Jk': 4, 'GEKzZ[': 4, 'GEK|Z[': 4, 'GBiiy{': 4, 'GBKz][': 4, 'GCsxzk': 4, 'G@L~Ms': 4, 'GEKxz[': 4, 'GWKy}{': 4, 'GHox}{': 4, 'GAT|t{': 4, 'G@wzm{': 4, 'GEKzZ{': 4, 'GDK}Z{': 4, 'GEKz^{': 4, 'GIKx}{': 3, 'G@Lzu{': 4, 'G@Lzt{': 3, 'G@Lzv{': 3, 'GBK|][': 4, 'GKSxx{': 4, 'GAkxzk': 4, 'G@K|zw': 4, 'GKKx}{': 4, 'G@Mzu{': 4, 'GPKyz{': 4, 'G@Mzv{': 4, 'GXKy}{': 3, 'GHK}}{': 3, 'G@L|~s': 3, 'GHK}~{': 3, 'G@L~r{': 3, 'G@Mzz{': 3, 'G@Lz~{': 3, 'G@Mz~{': 3, 'G@L~~{': 3, 'G@N~vs': 3, 'G@N^~w': 3, 'G@L~~w': 3, 'G@N~v{': 3, 'G@N~~{': 3, 'GBZbs{': 4, 'GDjbq{': 4, 'GxTP[{': 3, 'GBY[~K': 3, 'GBW{~K': 4, 'GIM]\\k': 4, 'GiKu\\{': 3, 'GDh^J{': 4, 'GIMuZ{': 3, 'GIMu^{': 3, 'G@\\u^c': 3, 'GBXr[{': 4, 'GINJls': 4, 'GIKx}[': 3, 'GIox|k': 3, 'GBdrZ[': 4, 'GC]jjk': 4, 'GILu\\{': 4, 'GIK}\\{': 3, 'GBXkz{': 3, 'GBdj\\{': 4, 'G_\\rl{': 3, 'GBXk~{': 3, 'GZW]K{': 4, 'GBfbZs': 4, 'G_ltjs': 3, 'GYQ[x{': 3, 'G_mrrk': 3, 'GbYa|{': 3, 'GSozj{': 3, 'GFXe\\{': 3, 'GIo|j{': 3, 'GPY]j{': 4, 'GpIYz{': 3, 'GIo|n{': 3, 'GBxk~k': 3, 'GINL|{': 3, 'GBY^n[': 3, 'GINJ|{': 3, 'GIo~l{': 3, 'GINL~{': 3, 'GC\\zvK': 3, 'GB\\s~[': 3, 'GBYZz{': 3, 'GC\\r~[': 3, 'GBYZ~{': 3, 'GBU|v[': 4, 'GBY\\~[': 4, 'GC\\tz{': 4, 'GAmrz{': 4, 'G@vTz{': 4, 'GAmr~[': 4, 'GDhZ~{': 4, 'GA]|vK': 4, 'G_]|rk': 3, 'GCxzvk': 3, 'G_\\t|{': 3, 'G_\\t~{': 3, 'GBY^~w': 3, 'GBY^~{': 3, 'G@FnUo': 4, 'GRWW}K': 4, 'GRG]]W': 4, 'G?\\s~_': 4, 'GB`k~O': 4, 'GFGm]W': 3, 'GGS}lo': 4, 'GXDYs[': 4, 'GoLYpk': 4, 'GMo\\H{': 4, 'GEo~@{': 3, 'GC\\v@{': 4, 'GcUj`{': 4, 'GiePX{': 4, 'G_lr`{': 4, 'GYeQX{': 3, 'GDh^B{': 4, 'GsKqZ{': 3, 'GIMuR{': 3, 'GIMuV{': 3, 'G?l~f_': 4, 'G`Q|ro': 3, 'G`hZtg': 4, 'GBmq^C': 4, 'G@d~V_': 4, 'G`Izuo': 4, 'G@NvUo': 3, 'GBze`{': 4, 'GbY^@{': 4, 'GiUtP{': 4, 'GRr@x{': 3, 'Gdh`y{': 4, 'Gbe`z[': 4, 'GLj@y{': 3, 'GDV`~S': 4, 'G_lp~c': 4, 'G@zP~c': 3, 'GEnfB{': 3, 'GLr@z{': 3, 'GRZCz{': 3, 'GqLcz{': 4, 'GRr@~{': 3, 'G@\\u^_': 3, 'GJY^C{': 3, 'G_ltrk': 4, 'GqOxx{': 3, 'GRZA|{': 4, 'GsOxz{': 3, 'GCxrj{': 3, 'GAytj{': 4, 'G_]tj{': 3, 'GCxrn{': 3, 'G_lvvg': 4, 'GsPx~s': 3, 'Gk_zz{': 3, 'G_lvvk': 3, 'Gi_z|{': 3, 'GYIZ}{': 4, 'GYQZ|{': 3, 'Gk_z~{': 3, 'GAmzvK': 4, 'G_mzrk': 3, 'GC\\~Vk': 3, 'GC^bz{': 3, 'G_ltz{': 3, 'GC^b~{': 3, 'G@\\v]w': 4, 'G@lv]w': 4, 'G@^mvk': 4, 'GAndz{': 4, 'G@zRz{': 4, 'G@zTz{': 4, 'G@zR~{': 4, 'G@zV~w': 3, 'G@zV~{': 3, 'GXvV?{': 3, 'GLh]vK': 3, 'GMox~K': 3, 'GIltm[': 4, 'GIM|u[': 3, 'GaLl|w': 4, 'GSprzw': 3, 'GBM^^W': 4, 'GBdv^W': 4, 'GEK~^W': 3, 'GAlnng': 4, 'G]_}Z{': 3, 'GS\\uZ{': 3, 'GBfnR{': 3, 'GDVnR{': 4, 'GFbnR{': 3, 'GBfnV{': 3, 'G@z^vg': 3, 'GFN^V[': 3, 'GFo~^[': 3, 'GFdn^{': 3, 'GBfn^s': 3, 'Godzz{': 3, 'GC^vn[': 3, 'GENn^{': 3, 'G@z^vk': 3, 'G@vv^s': 3, 'G_nrz{': 3, 'G_^t~{': 3, 'GENn~{': 3, 'GFXj[{': 3, 'GC|rnK': 3, 'GB^fK{': 3, 'GBX{~S': 4, 'GB]k~K': 4, 'GBd~NS': 4, 'GCLz~o': 4, 'GC\\z^c': 4, 'G@N]~o': 3, 'GAmz^c': 4, 'GiK}\\{': 3, 'GI]u\\{': 4, 'GB]^J{': 3, 'GDl^J{': 4, 'G_\\~d{': 3, 'GB]^N{': 3, 'GByZ~k': 3, 'GBfnZ{': 3, 'GB]^n[': 3, 'GC^r~[': 3, 'GBd~^{': 3, 'GBdz~[': 3, 'GC\\zz{': 3, 'GClzz{': 4, 'GC\\z~[': 3, 'GC\\z~{': 3, 'GA^t|{': 4, 'GC^tz{': 4, 'GAmzz{': 4, 'G@v\\z{': 4, 'GAmz~{': 4, 'GAmz~[': 4, 'G_mzz{': 3, 'GC\\~^{': 3, 'GC\\~~{': 3, 'GIllmk': 4, 'GEwznK': 4, 'GFijY{': 4, 'GBmi~K': 4, 'GBX^\\w': 4, 'GBMn]w': 4, 'G@^fmw': 4, 'GBlk~K': 4, 'GD\\i~K': 4, 'GEMz^S': 4, 'GAl~Nc': 4, 'GAN\\~o': 4, 'GClz^c': 4, 'GEKz~W': 4, 'G@T~^o': 4, 'G@d~^o': 4, 'GiW{|{': 4, 'GIY}t{': 4, 'Gg\\\\l{': 4, 'GCnrr{': 4, 'G@^^b{': 4, 'GDN^R{': 4, 'GA^nd{': 4, 'G@^^f{': 4, 'GBVnt{': 4, 'GBNn]{': 4, 'GBU~v[': 4, 'G@^\\~k': 4, 'G@^^n{': 4, 'GA}r~k': 4, 'GEL~^[': 4, 'GGnr}{': 4, 'GAl~n{': 4, 'G@\\}~k': 4, 'GAlz~k': 4, 'G@tzz{': 4, 'G@uzz{': 4, 'G@tz~{': 4, 'GEMz~[': 4, 'G@uz~{': 4, 'G@t~~{': 4, 'GENnfS': 3, 'G@|vMk': 4, 'G_l~fc': 3, 'GF`z^S': 3, 'GGlvmw': 4, 'GBdnnW': 3, 'GAM~^o': 4, 'G_Mz~o': 4, 'G@Nm~o': 3, 'G{`Xz{': 3, 'G[`}r{': 3, 'GC^nb{': 3, 'G@z^b{': 4, 'G@z^f{': 3, 'G@^v]{': 4, 'G@\\~]{': 4, 'G@l~]{': 4, 'G@^m~{': 4, 'G@z^~{': 3, 'G@~^nk': 3, 'GC^v~w': 3, 'GC\\~~w': 3, 'G@t~~w': 4, 'G@z^~w': 3, 'G@v~v{': 3, 'GC^~~{': 3, 'GD\\c~K': 4, 'GBYsz[': 4, 'GBdlvK': 4, 'GHhY{{': 4, 'GIqX|k': 4, 'GDdjvK': 4, 'GO]ri{': 4, 'GDUjj[': 4, 'GC^Rl[': 4, 'GHUt]{': 4, 'GSpXz{': 4, 'GPTt]{': 4, 'GBiZZ{': 4, 'GDhiz{': 4, 'GDqiz{': 4, 'GO]rm{': 4, 'GBhk~{': 4, 'GJQjs{': 4, 'GPXY{{': 4, 'GaKxz[': 4, 'GWTX{{': 4, 'GbOx|[': 4, 'GDUrZ[': 4, 'GGlri{': 4, 'G@ujjk': 4, 'GIdr\\{': 4, 'GaKz\\{': 4, 'GDXi|{': 4, 'GDXiz{': 4, 'GELj\\{': 4, 'GGtrl{': 4, 'GDXi~{': 4, 'G@nbuk': 4, 'GBZL[{': 4, 'GWMY}k': 4, 'GC^Tj[': 4, 'G@urj[': 4, 'GPozm{': 4, 'GoS{z{': 4, 'GBqkz{': 4, 'GEgzZ{': 4, 'G@yrm{': 4, 'GEMj^{': 4, 'GZTc[{': 4, 'GDVdr[': 4, 'G@zRrk': 4, 'G@zTrk': 4, 'GBfdr[': 4, 'G`iqzs': 4, 'GYI[y{': 4, 'GJFJ\\s': 4, 'GDfbr[': 4, 'GpTa|{': 4, 'Gp_yz{': 4, 'GLXU\\{': 4, 'GO]uj{': 4, 'GGttj{': 4, 'G@yuj{': 4, 'GOurj{': 4, 'GGttn{': 4, 'GDla~K': 4, 'GDTlvK': 4, 'GPhYy{': 4, 'GHX[{{': 4, 'GBrLX{': 4, 'GIY[|k': 4, 'G@^Ul[': 4, 'GPUr]{': 4, 'GShYz{': 4, 'GDdjZ{': 4, 'GBiiz{': 4, 'GDrHz{': 4, 'GG]tm{': 4, 'GBii~{': 4, 'GHVJls': 4, 'GILr[{': 4, 'G@\\vUk': 4, 'GIgxy{': 4, 'G@]jmk': 4, 'GHTu\\{': 4, 'G`Tr\\{': 4, 'GIgy|{': 4, 'GBhi|{': 4, 'GHX[z{': 4, 'GBLm\\{': 4, 'GJDm\\{': 4, 'GHX[~{': 4, 'G@lvUk': 4, 'G@nbms': 4, 'GHp[x{': 4, 'GPpYx{': 4, 'GPS~M{': 4, 'GWczm{': 4, 'GSX[z{': 4, 'GDpkz{': 4, 'GBg}Z{': 4, 'GDLmZ{': 4, 'G@]vM{': 4, 'GBMm^{': 4, 'GwSzc{': 4, 'GIY\\tk': 4, 'GIS|l[': 4, 'GHM]m[': 4, 'G@]]nK': 4, 'G@[~Mk': 4, 'GbLe\\{': 4, 'GSdrZ{': 4, 'GClvJ{': 4, 'G@^ej{': 4, 'G@nej{': 4, 'G@^en{': 4, 'GDxi~k': 4, 'GaLl|{': 4, 'GHo~m{': 4, 'GDXZ~[': 4, 'GaLl~{': 4, 'GHtk~k': 4, 'GIY\\|{': 4, 'GIY\\~{': 4, 'GBezv[': 4, 'GBiZ~[': 4, 'GBh\\~[': 4, 'GClrz{': 4, 'GAltz{': 4, 'GAlt~[': 4, 'GDdj~{': 4, 'GB\\\\n[': 4, 'GIYZ|{': 4, 'GBUjz{': 4, 'GBUj~{': 4, 'GDszn[': 4, 'GELl~[': 4, 'GBNL~[': 4, 'G@uuz{': 4, 'GELlz{': 4, 'GEMjz{': 4, 'G@^d}{': 4, 'GDNJ~{': 4, 'G@\\~Uk': 4, 'G@l~Uk': 4, 'GAx|vk': 4, 'GbO|~[': 4, 'GIY\\~k': 4, 'GG^R|{': 4, 'GA^d|{': 4, 'GG^T~{': 4, 'GBUn~w': 4, 'GBUn~{': 4, 'GBXi|{': 4, 'GISx|{': 3, 'GISx~{': 3, 'GLTX~[': 3, 'GIS||{': 3, 'GBXm|{': 3, 'GBX^\\{': 4, 'GISz|{': 3, 'GIK}|{': 3, 'GIS|~{': 3, 'GDTzv[': 4, 'GA\\t|{': 4, 'GA\\r|{': 4, 'G@\\u|{': 4, 'G@\\v]{': 4, 'GA\\t~{': 4, 'GHLzu{': 3, 'G@\\tz{': 3, 'G@\\r~{': 3, 'GPLzu{': 3, 'G@mrz{': 3, 'G@\\t~{': 3, 'G@\\v~w': 3, 'G@\\v~{': 3, 'GKhYx{': 4, 'GISx{{': 4, 'GIgx}{': 4, 'GIUX|{': 4, 'GQWx}{': 4, 'GBhh}{': 4, 'GSKyz{': 4, 'GKSxz{': 4, 'GKSx~{': 4, 'GMcx~[': 4, 'GHM]}{': 4, 'GQK~]{': 4, 'GQK}z{': 4, 'GKK}z{': 4, 'GKK}~{': 4, 'GEMzv[': 4, 'GDLn]{': 4, 'G@lu}{': 4, 'GDLmz{': 4, 'G@lv]{': 4, 'G@lu~{': 4, 'GLKz]{': 4, 'GPLZz{': 4, 'G@ltz{': 4, 'GPLZ~{': 4, 'G@lv~w': 4, 'G@lv~{': 4, 'GLiiy{': 3, 'GIY\\|w': 4, 'GBS~^W': 4, 'G@^Nng': 3, 'GMoxx{': 3, 'GbXk|{': 3, 'GSdzr{': 3, 'GBVnT{': 4, 'GHN]r{': 3, 'GPN]r{': 3, 'GHN]v{': 3, 'GXL}u{': 3, 'GYK}}{': 3, 'GIU~t{': 3, 'G@nr~s': 3, 'GXL]~{': 3, 'GIU||{': 3, 'GHN]|{': 3, 'GHN]~{': 3, 'G@l~vk': 3, 'G@lz~k': 3, 'G@]~n{': 3, 'GHN^~{': 3, 'GLTZ\\[': 4, 'GFTj\\[': 4, 'GYTXx{': 3, 'G[TXx{': 3, 'GBL}^S': 4, 'GJTX|[': 4, 'GB\\X~K': 4, 'G@\\}^c': 3, 'G@Lz~o': 3, 'GiSx|{': 3, 'GIT|t{': 4, 'GA\\~d{': 4, 'G@\\~b{': 3, 'G@\\~d{': 3, 'G@\\~f{': 3, 'G@^r~s': 3, 'GHL}}{': 3, 'G@\\~vk': 3, 'G@]~j{': 3, 'G@^r~{': 3, 'G@^rz{': 3, 'G@lzz{': 3, 'G@\\z~{': 3, 'G@mzz{': 3, 'G@lz~{': 3, 'G@\\~~{': 3, 'GMK|][': 3, 'GFMj][': 4, 'GBM}^S': 4, 'GIsx|k': 3, 'GAMz~o': 4, 'G@l}^c': 3, 'G@Mz~o': 3, 'G[Sx}{': 3, 'GMK|]{': 3, 'G@l~e{': 4, 'G@l~b{': 3, 'G@l~f{': 3, 'G@l~~{': 3, 'G@~vj{': 3, 'G@^v~w': 3, 'G@\\~~w': 3, 'G@l~~w': 3, 'G@^~v{': 3, 'G@^~~{': 3, 'GrXk{{': 3, 'GFo~^W': 3, 'GYK}}w': 3, 'GAN~vo': 4, 'G@r~vo': 3, 'G@N~vo': 3, 'GrY[z{': 3, 'GFzcz{': 3, 'G@~vb{': 3, 'G@~vf{': 3, 'G@~vvk': 3, 'GXN]}{': 3, 'G@~vn{': 3, 'G@~~vk': 3, 'G@~v~{': 3, 'G@~~~{': 3, 'GIS||w': 3, 'GAmrzw': 4, 'G@]|rk': 3, 'GIM|u{': 3, 'GDhzr{': 3, 'GBmr]{': 3, 'GBmr^{': 3, 'GBlnMk': 4, 'GIM^nW': 4, 'GhX[|{': 3, 'GSNZr{': 3, 'GBZmt{': 3, 'GIN\\r{': 3, 'GIN\\v{': 3, 'GBZ\\~o': 3, 'GXdzu{': 3, 'GP\\u}{': 3, 'GBmr~[': 3, 'GBY~u{': 3, 'GP\\u~{': 3, 'GDhzz{': 3, 'GBZ\\|{': 3, 'GBY|z{': 3, 'GIN\\|{': 3, 'GDhz~{': 3, 'GBX}|{': 3, 'GIM~]{': 3, 'GBZ\\~{': 3, 'GB\\t~[': 3, 'GD\\r~[': 3, 'GBYzz{': 3, 'GBYz~{': 3, 'GIM~u{': 3, 'GIL}|{': 3, 'GIN\\~{': 3, 'GBY~~{': 3, 'GSSzzw': 4, 'GEXzt[': 4, 'GB\\u\\[': 4, 'GILzs{': 4, 'GClrzw': 4, 'G@lrzw': 4, 'GBTzt[': 4, 'GaLzt{': 4, 'GIdzt{': 4, 'GDXzt{': 4, 'GEXzt{': 4, 'GDXzr{': 4, 'GItp|{': 4, 'GDXzv{': 4, 'GB\\r[{': 3, 'GB\\r\\{': 3, 'GJXX~{': 3, 'GS\\zrk': 3, 'GJ\\r[{': 3, 'Gb\\r\\{': 3, 'GJX\\|{': 3, 'GJX\\~{': 3, 'GJXZ|{': 3, 'GILz~{': 3, 'GIL~~{': 3, 'GIN~vs': 3, 'GBY~~w': 3, 'GIL~~w': 3, 'GIN~v{': 3, 'GIN~~{': 3, 'GAH}to': 4, 'GBZLSk': 4, 'GBrLPk': 5, 'G`Xksk': 4, 'G@lvA{': 4, 'GC^Tb[': 4, 'GsDXr[': 4, 'GS\\Sj[': 4, 'GDZ@x{': 4, 'GBqax{': 4, 'GYEIx{': 4, 'GBqb[{': 4, 'GR`Kz[': 4, 'G`hTY{': 4, 'G@lvE{': 4, 'GDZ@z{': 4, 'GBqcz{': 4, 'GqG[z{': 4, 'GRQKz{': 4, 'GDZ@~{': 4, 'G_K|rg': 4, 'G`qipk': 4, 'GdKjI{': 4, 'G[S[j[': 4, 'GKU\\b[': 5, 'GQNAx{': 4, 'G`hPx{': 4, 'GoSqx{': 4, 'GBqeX{': 4, 'GR`LY{': 4, 'G`hUX{': 5, 'G`MrU{': 4, 'GpDHz{': 4, 'GYEKz{': 4, 'GHqSz{': 4, 'G`hP~{': 4, 'G?l|bc': 4, 'G`hkqk': 4, 'GDhrQ{': 4, 'GSS}b[': 4, 'GIeax{': 4, 'GRQIx{': 4, 'GR`Hx{': 4, 'GR`MX{': 4, 'G`YTY{': 4, 'GD]bM{': 4, 'GSXPz{': 4, 'GQNCz{': 4, 'GR`H~{': 4, 'GBqbzw': 4, 'GDZDzw': 4, 'G`hTzw': 4, 'GR`Lzw': 4, 'GBqb~w': 4, 'GBqbz{': 4, 'GDZDz{': 4, 'G`hTz{': 4, 'GR`Lz{': 4, 'GBqb~{': 4, 'GqG^~w': 4, 'GqG^~{': 4, 'GRmRI[': 4, 'GZSmK{': 4, 'GBox~K': 4, 'GDYY~K': 4, 'GPS}j[': 4, 'G`hZtk': 4, 'GKhZtk': 4, 'GMWu\\{': 4, 'GPo}j{': 4, 'GIdlj{': 4, 'GPUmj{': 4, 'G`iqz{': 4, 'GSUjj{': 4, 'GhUa|{': 4, 'GIdln{': 4, 'GTdrQ[': 5, 'GAL~fO': 4, 'GSXZtk': 4, 'GJqax{': 4, 'GH^VC{': 4, 'GWS{}k': 4, 'GIiY|k': 4, 'GoSxzk': 4, 'G[QYx{': 4, 'GId\\l[': 4, 'G`czj[': 4, 'GKpX|k': 4, 'G`h\\rk': 4, 'GSSzj[': 4, 'GKiYzk': 4, 'GKh\\rk': 4, 'GBr`zs': 4, 'GDZdq{': 4, 'GJjA|{': 4, 'GdO|Z{': 4, 'G`UtZ{': 4, 'GQY\\j{': 4, 'GKhZj{': 4, 'GQo|j{': 4, 'GXVA|{': 4, 'GKhZn{': 4, 'G`X\\tg': 4, 'G_l|bc': 4, 'G@lu^_': 4, 'G`Mr]o': 4, 'GD\\tUK': 4, 'GIne`{': 4, 'Ga]v@{': 4, 'GDz@zk': 4, 'GdhPz[': 4, 'Gr`Hx{': 4, 'GDZ`}s': 4, 'G`hX~c': 4, 'GRYP}[': 4, 'GMnDJ{': 4, 'GiiPz{': 4, 'GYNCz{': 4, 'Gr`H~{': 4, 'GQKx}[': 4, 'GUOxz[': 4, 'G`Xk{{': 4, 'GKhY|k': 4, 'GDW~M{': 4, 'GQK}Z{': 4, 'G`Y[z{': 4, 'G[Ox}{': 4, 'GQK}^{': 4, 'G`Llms': 4, 'G`Uhzk': 4, 'GIeZ\\k': 4, 'G`K|Y{': 4, 'G`qix{': 5, 'G`Mr]{': 4, 'GpCz]{': 4, 'G`gyz{': 4, 'GKh[z{': 4, 'G`Mi~{': 4, 'GD]bm[': 4, 'GPUZj[': 4, 'GRO{z[': 4, 'GHd]l[': 4, 'GKK|Y{': 4, 'G`hky{': 4, 'GBir]{': 4, 'GR_z]{': 4, 'GQMZZ{': 4, 'G`h[z{': 4, 'GKMi~{': 4, 'GQo~vg': 4, 'GQrp~s': 4, 'GqIZz{': 4, 'GRQZ~[': 4, 'GM_z~[': 4, 'GQo~vk': 4, 'GqIZ~{': 4, 'GK\\\\^k': 4, 'GKUjz{': 4, 'GQNLz{': 4, 'G`h\\z{': 4, 'GQdlz{': 4, 'GKUj~{': 4, 'G`h^~w': 4, 'G`h^~{': 4, 'GDjJrk': 4, 'GySp[{': 4, 'GINbs{': 4, 'GBY]l[': 4, 'GIM]l[': 4, 'GBYp}[': 4, 'GIM[~K': 4, 'GjG]\\{': 4, 'GDhuZ{': 4, 'GINcz{': 4, 'GINc~{': 4, 'G`MZj[': 4, 'GJ`ix{': 4, 'GPUji{': 4, 'GHdrY{': 4, 'GQKzY{': 4, 'G`KzY{': 4, 'GJ`i|{': 4, 'GHpq|{': 4, 'GQLi|{': 4, 'G`Li|{': 4, 'GKXXz{': 4, 'GKXX~{': 4, 'GHx[~k': 4, 'GBZL|{': 4, 'GIc~n[': 4, 'GBZJ|{': 4, 'GIM^n[': 4, 'GBZL~{': 4, 'GLdX~[': 4, 'GBhl}{': 4, 'GSSzz{': 4, 'GQLl}{': 4, 'GIM]|{': 4, 'GKS|z{': 4, 'GIMl}{': 4, 'GSLZ~{': 4, 'GKxX~k': 4, 'G`X\\|{': 4, 'G`X\\~{': 4, 'GJS{~[': 4, 'GKSz~[': 4, 'GIMZz{': 4, 'GIMZ~{': 4, 'GIM^~w': 4, 'GIM^~{': 4, 'G?T|v_': 4, 'G@Q~Uo': 4, 'GFOm\\W': 4, 'GBbH~O': 5, 'GBJK~O': 4, 'GYKW}K': 4, 'GGT\\tg': 4, 'GR`KzW': 4, 'GrOkW{': 4, 'GGD}to': 4, 'GYSXk[': 4, 'GGTs|o': 4, 'GQ[XmK': 4, 'GLPL[w': 4, 'GLO\\]W': 4, 'GK`\\Zo': 4, 'GRSZK[': 4, 'GoDXzo': 4, 'GBFL^O': 4, 'GAuv@{': 4, 'G@^e`{': 4, 'GkS\\H{': 4, 'GaUtP{': 4, 'GDX^@{': 4, 'G_ur`{': 4, 'GkdPX{': 4, 'Gcoz`{': 4, 'GMdLH{': 4, 'G`drP{': 4, 'GSXZ`{': 4, 'GMf@X{': 4, 'GWd]`{': 4, 'G@neb{': 4, 'GClvB{': 4, 'G@^eb{': 4, 'GdMaZ{': 4, 'GSdrR{': 4, 'G@^ef{': 4, 'GRO\\]W': 4, 'GBRL\\o': 4, 'GP[YmK': 4, 'GR`MXw': 4, 'GKFLZo': 4, 'GZCY[[': 4, 'G?\\utg': 4, 'GBbJ\\o': 5, 'GGS}tg': 4, 'GGS{~_': 4, 'GoTXpk': 4, 'GMULH{': 4, 'GmEHX{': 4, 'GEqrP{': 4, 'GD\\eH{': 4, 'GcUrP{': 4, 'GcS~@{': 4, 'G[dQX{': 4, 'G`lah{': 4, 'GDhuR{': 4, 'GtGYZ{': 4, 'GINcr{': 4, 'GINcv{': 4, 'GDlq^C': 4, 'G`h\\rg': 4, 'GD]ZNC': 4, 'G`MzeS': 4, 'GB]tUK': 4, 'G@lvUg': 4, 'G@l~Ec': 4, 'GJjM`{': 4, 'G`^e`{': 4, 'GbYuP{': 4, 'Gi]ch{': 4, 'GTZ@y{': 4, 'GdZ@x{': 4, 'Gdd`z[': 4, 'G`jPzs': 4, 'GSV`zs': 4, 'G`l`}k': 4, 'GJiP}[': 4, 'GDZP~S': 4, 'GD^@~K': 4, 'GKuvB{': 4, 'Gbj@z{': 4, 'GJqcz{': 4, 'GZQKz{': 4, 'GwSsz{': 4, 'GdZ@~{': 4, 'G@\\vUg': 4, 'G`Yszs': 4, 'GJZTS{': 4, 'GD^Dj[': 4, 'GBjLrk': 4, 'GWeYzk': 4, 'GHqY|k': 4, 'GPozi{': 4, 'GDW}m[': 4, 'GZQI|{': 4, 'GoUpz{': 4, 'GEhrZ{': 4, 'GBqtZ{': 4, 'GEhr^{': 4, 'GIL~Cs': 4, 'GZTLK{': 4, 'GDnBj[': 4, 'GI]bk{': 4, 'G`Wx}k': 4, 'GRO|Y{': 4, 'GIeZl[': 5, 'GBqjrk': 4, 'GEYpz[': 4, 'GDY]j[': 4, 'GPS~I{': 4, 'GJYU\\{': 4, 'GpC}Z{': 4, 'GSYqz{': 4, 'GxDI|{': 4, 'GPqqz{': 4, 'GHpsz{': 4, 'GPUuZ{': 4, 'GHps~{': 4, 'G`iZrk': 4, 'GZLMK{': 4, 'GHd[~K': 4, 'GROx}[': 4, 'G`hszs': 4, 'GIc}l[': 4, 'G`Ypy{': 4, 'GD^Bl[': 4, 'GDZLrk': 4, 'GBqrZs': 4, 'GBi]j[': 4, 'GBqpz[': 4, 'GPSzm[': 4, 'GNHM\\{': 4, 'GSW}j{': 4, 'GoMqz{': 4, 'GjII|{': 4, 'GDqjj{': 4, 'GDYmj{': 4, 'GBplj{': 4, 'GBpln{': 4, 'GBmbm[': 4, 'GDhZj[': 4, 'GBYtY{': 4, 'GIK|[{': 4, 'GDhr]{': 4, 'GL_z]{': 4, 'GSLiz{': 4, 'GPp[z{': 4, 'GIMkz{': 4, 'GIMk~{': 4, 'GoS~vg': 4, 'GdRh~s': 4, 'GYaZz{': 4, 'Gh_z}{': 4, 'GoS~vk': 4, 'Ggcz~k': 4, 'GIiZ~k': 4, 'GYEZ~[': 4, 'GYaZ~{': 4, 'GS\\i~k': 4, 'GSXZz{': 4, 'GIiZ|{': 4, 'GSXZ~{': 4, 'GE\\l^k': 4, 'GcLlz{': 4, 'GEYjz{': 4, 'GBjLz{': 4, 'GEhlz{': 4, 'GEYj~{': 4, 'GB^L^k': 4, 'GBqjz{': 4, 'GBqj~{': 4, 'GBqn~w': 4, 'GBqn~{': 4, 'GKTzt[': 4, 'GS\\rY{': 4, 'G`X\\|w': 4, 'GM`zt[': 4, 'GHM]}w': 4, 'GMW}\\{': 4, 'GQ\\sz{': 4, 'GK\\u\\{': 4, 'G`mqz{': 4, 'GKmqz{': 4, 'GcXzt{': 4, 'GQ\\s~{': 4, 'GTX]vK': 4, 'GKtrl[': 4, 'GJdml[': 4, 'GKlZnK': 4, 'GN`Z\\[': 4, 'GQMzu[': 4, 'G`Mz]s': 4, 'GQMz]s': 4, 'GM`z\\s': 4, 'GQK~]w': 4, 'GIdnlw': 4, 'G[duZ{': 4, 'GK^Lj{': 4, 'GKVlr{': 4, 'GEjvR{': 4, 'GQNmv{': 4, 'GBlvM[': 4, 'G`h\\zw': 4, 'GIM]|w': 4, 'GK\\X~K': 4, 'GId~d[': 4, 'GUSxz[': 4, 'GMX\\\\{': 4, 'GkWy|{': 4, 'GdczZ{': 4, 'GK\\^L{': 4, 'GRS}Z{': 4, 'GLc}Z{': 4, 'GE\\nL{': 4, 'GRS}^{': 4, 'GJd^L[': 4, 'GJS}\\[': 4, 'GRhky{': 4, 'GQdlzw': 4, 'GKUxzs': 4, 'GIiZ|w': 4, 'GK\\Z\\k': 4, 'GId~Ls': 4, 'GKsxzk': 4, 'GJUm\\{': 4, 'GbLm\\{': 4, 'GSlZj{': 4, 'G`\\ml{': 4, 'GPl]j{': 4, 'GI]\\j{': 4, 'GB^e\\{': 4, 'GI]\\n{': 4, 'GNd\\^[': 4, 'GRd^^[': 4, 'GLU^^{': 4, 'GRUZ~[': 4, 'GQdzz{': 4, 'G`fjz{': 4, 'GaM|z{': 4, 'GKU|z{': 4, 'GcLz~[': 4, 'GQdz~{': 4, 'GKh}~s': 4, 'GKL~]{': 4, 'GDZ^n[': 4, 'GQNm~{': 4, 'GQNZ~s': 4, 'GQLz}{': 4, 'GKN\\z{': 4, 'GQL}~{': 4, 'GHuZ~k': 4, 'GIdz|{': 4, 'GId|~{': 4, 'GBq~^s': 4, 'GBjm~s': 4, 'GaL|~[': 4, 'GHfmz{': 4, 'GWdz}{': 4, 'GaM~^{': 4, 'GQd~~{': 4, 'G@mzrk': 4, 'GAmzrk': 4, 'GKkzm{': 4, 'GDlrZ{': 4, 'GDlr]{': 4, 'GDlr^{': 4, 'GB^\\nS': 4, 'GXlq}{': 4, 'GJMm}{': 4, 'GQ[}~k': 4, 'GH]]~k': 4, 'GDlr~[': 4, 'GB]nm{': 4, 'GLLm~{': 4, 'GD\\j~k': 4, 'GPTzz{': 4, 'GPUzz{': 4, 'GPTz~{': 4, 'GDYz~{': 4, 'GPT~~{': 4, 'GMpp|[': 4, 'GQd~fS': 4, 'GFpr\\[': 4, 'GIlvK{': 4, 'GExrl[': 4, 'GEh~fS': 4, 'GElr^K': 4, 'GM`x~S': 4, 'GaK|~W': 4, 'GSLz]s': 4, 'GaMlzw': 4, 'GHd^nW': 4, 'GHdv]w': 4, 'GEhznS': 4, 'G]`kz{': 4, 'G\\`]Z{': 4, 'GS\\mj{': 4, 'GMa~R{': 4, 'GDZmr{': 4, 'GBrlr{': 4, 'GD^NJ{': 4, 'GBrlv{': 4, 'GHd}nS': 4, 'GB^el[': 4, 'GBX}\\s': 4, 'GBizu[': 4, 'GB]l]k': 4, 'GE\\j\\k': 4, 'GEhlzw': 4, 'GBmj]k': 4, 'GEMzr[': 4, 'G@v\\rk': 4, 'GI]ml{': 4, 'Gg[}l{': 4, 'GB^TZ{': 4, 'GDnRZ{': 4, 'GB^T^{': 4, 'GBY^nW': 4, 'GBXm|w': 4, 'GEhzvK': 4, 'GEXl|w': 4, 'GBY|u[': 4, 'G@vTzw': 4, 'GEMjzw': 4, 'GINmt{': 4, 'Gg\\s|{': 4, 'GDjZr{': 4, 'GBZ\\r{': 4, 'GBZ\\v{': 4, 'GBze|w': 4, 'GB^\\vK': 4, 'GFZ\\v[': 4, 'GBuv^[': 4, 'GBur~[': 4, 'GBuv^{': 4, 'GBuj~k': 4, 'GBpz|{': 4, 'GDZ\\z{': 4, 'GBp|~{': 4, 'GEY|z{': 4, 'GEhzz{': 4, 'GEhz~{': 4, 'GEh~~{': 4, 'GDZ~vs': 4, 'GHf^~w': 4, 'GPT~~w': 4, 'GDZ^~w': 4, 'GDZ~v{': 4, 'GDZ~~{': 4, 'GLN]v[': 3, 'GPvRz{': 3, 'GBze|{': 3, 'GHvR|{': 3, 'GRYZ}{': 3, 'GRY^]{': 3, 'GPvR~{': 3, 'GLmrY{': 4, 'GLhzu{': 3, 'GS\\rz{': 3, 'GLh\\z{': 3, 'GS\\r~{': 3, 'GLh^~w': 3, 'GLh^~{': 3, 'GqK{z[': 3, 'GULjY{': 4, 'GMMlY{': 3, 'GbMj[{': 4, 'GMTh|[': 4, 'GUMjY{': 4, 'G[dYx{': 3, 'GdXi|{': 3, 'GLX]\\{': 4, 'GsKyz{': 3, 'GYS{z{': 3, 'G[cyz{': 3, 'GFXm\\{': 3, 'GYS{~{': 3, 'GTXzu{': 4, 'GJY\\|{': 4, 'GQ\\u|{': 4, 'GJY]|{': 4, 'GQ\\tz{': 4, 'GJUm|{': 4, 'GQ\\t~{': 4, 'GpLzu{': 3, 'G`mrz{': 3, 'G`\\tz{': 3, 'G`\\t~{': 3, 'GTXZzw': 4, 'GJ\\u\\{': 3, 'GJYZz{': 3, 'GJYZ~{': 3, 'GP\\~e{': 3, 'GYS}|{': 3, 'GB^dz{': 3, 'GDnbz{': 3, 'GB^e|{': 3, 'GB^d~{': 3, 'GJY^~w': 3, 'GJY^~{': 3, 'GqLzs{': 3, 'GP\\u}w': 3, 'G`]|rk': 3, 'GXf]r{': 3, 'Gdhzr{': 3, 'GLvTZ{': 3, 'Gbmr^{': 3, 'GjY}t{': 3, 'GjY\\|{': 3, 'GjY\\~{': 3, 'Gbmr~[': 3, 'Gdhzz{': 3, 'Gdhz~{': 3, 'GbY~~{': 3, 'GRd^^W': 4, 'GYT\\|w': 3, 'GNrLX{': 3, 'GJe^^W': 3, 'GH]u}w': 4, 'GQ\\u|w': 4, 'GB]|vK': 3, 'GHN]~o': 3, 'GBfn^o': 3, 'GpN]r{': 3, 'GRvTZ{': 4, 'GS\\~b{': 3, 'GT\\uZ{': 3, 'GPv^b{': 3, 'GJmu^{': 3, 'GLjZ~s': 3, 'GLh}}{': 3, 'GS\\~vk': 3, 'GLh}~{': 3, 'GS^rz{': 3, 'GS\\zz{': 3, 'GS\\z~{': 3, 'GIm~~{': 3, 'GInv~w': 3, 'GIm~~w': 3, 'GBz~v{': 3, 'GIn~~{': 3, 'GI}r~k': 3, 'GbY|z{': 3, 'GIl~n{': 3, 'GRYz}{': 3, 'GI]||{': 3, 'GJY|}{': 3, 'GImz~{': 3, 'GJY~u{': 3, 'GB\\~n[': 3, 'GB^v^{': 3, 'GI]~~{': 3, 'GIlz~k': 3, 'GImzz{': 3, 'GI\\|~{': 3, 'GI\\z|{': 3, 'GD\\zz{': 3, 'GB\\z~{': 3, 'GD\\z~[': 3, 'GBnjz{': 3, 'GDlzz{': 3, 'GD\\z~{': 3, 'GB\\~~{': 3, 'GPvrz{': 3, 'GPvZz{': 3, 'GD\\~^{': 3, 'GByz~k': 3, 'GHvZ|{': 3, 'GB]~n[': 3, 'GBnj~{': 3, 'GBmz~[': 3, 'GEmzz{': 3, 'GDlz~{': 3, 'GD\\~~{': 3, 'GF\\~^[': 3, 'GB^n~w': 3, 'GB\\~~w': 3, 'GD\\~~w': 3, 'GB^~v{': 3, 'GB^~~{': 3, 'G{Uj_{': 4, 'GD^fe[': 4, 'GLh^e[': 3, 'GMhX~K': 3, 'GLpq|[': 4, 'GRLk}[': 3, 'GFrdZ{': 3, 'GULmZ{': 3, 'GLVLZ{': 3, 'GMjLj{': 3, 'GRpk~{': 3, 'G{drO{': 3, 'GUozj[': 3, 'GIk~Mk': 3, 'GiK|[{': 3, 'GMqtZ{': 3, 'GsXXz{': 3, 'GFZLZ{': 3, 'GFqj^{': 3, 'G]dX~[': 3, 'GqMZz{': 3, 'GYMZ}{': 3, 'GFqnZ{': 3, 'GqMZ~{': 3, 'GLV\\v[': 3, 'GLp^\\{': 3, 'GRfJz{': 3, 'GRo~]{': 3, 'GRNJ}{': 3, 'GIur|{': 3, 'GBzV\\{': 3, 'GRqZ~{': 3, 'GHl~e{': 3, 'GD^bz{': 3, 'GD^dz{': 3, 'GD^b~{': 3, 'GBzmtk': 3, 'GBu~f[': 3, 'GBvb|{': 3, 'GEnbz{': 3, 'GFqj~{': 3, 'GD^f~w': 3, 'GD^f~{': 3, 'GrZH{{': 3, 'GRY^]w': 3, 'GYS}|w': 3, 'GYL{}s': 3, 'GFqnZw': 3, 'GIN\\~o': 3, 'GBrl~o': 4, 'G@l~vg': 3, 'G@^^no': 4, 'Gp^Sz{': 3, 'GRu^J{': 3, 'GD^nb{': 3, 'GFzTZ{': 3, 'GD^vV{': 3, 'GD~b~k': 3, 'G[N]z{': 3, 'GDx~n{': 3, 'GIn\\~k': 3, 'GS\\z}{': 3, 'GHn]~k': 3, 'GHv\\~{': 3, 'GD^nvk': 3, 'GD^r~[': 3, 'GD^^n[': 3, 'GD^v^{': 3, 'GBnn~{': 3, 'GBz\\~k': 3, 'GBzm|{': 3, 'GBz\\~{': 3, 'GBx}|{': 3, 'GDzZz{': 3, 'GB\\}|{': 3, 'GB^\\~{': 3, 'GEl~~{': 3, 'GFl~^[': 3, 'GBnn~w': 3, 'GEl~~w': 3, 'GD^~v{': 3, 'GD^~~{': 3, 'Gi]||{': 3, 'GI~vl{': 3, 'GF^n^{': 3, 'GB~v~{': 3, 'GB~~~{': 3, 'GIN~vo': 3, 'GlmrY{': 3, 'GI~vd{': 3, 'GFzbz{': 3, 'GFzdz{': 3, 'Gs\\tz{': 3, 'GFzb~{': 3, 'G]o~~w': 2, 'G]o~~{': 2, 'GDZ~vo': 4, 'G`N~vo': 2, 'Gb]|vK': 3, 'G@~~fc': 3, 'GK~vb{': 3, 'GF~fJ{': 3, 'G^rH~{': 2, 'G^zUX{': 3, 'Gs\\~vk': 3, 'GFx~n[': 3, 'GFzv^{': 3, 'G]pz|{': 3, 'Gs\\zz{': 2, 'Gs\\z~{': 2, 'GFzn~{': 2, 'GFzn~w': 2, 'GB~~vk': 3, 'GF~v^{': 2, 'GFz~~{': 2, 'GF~~~{': 2, 'GKcZJK': 4, 'GeGhW{': 4, 'GwC^?{': 3, 'GTPIX{': 4, 'G`NEH{': 3, 'GwCWx{': 3, 'GJaKZ{': 3, 'GwCWz{': 3, 'GwCW~{': 2, 'G?mzbc': 4, 'GIH{ss': 4, 'GDlbI{': 4, 'GST\\b[': 4, 'GTPHx{': 4, 'GJaIx{': 4, 'G`otY{': 4, 'GDlbM{': 4, 'GTPHz{': 4, 'GQUcz{': 4, 'GTPH~{': 4, 'GQTXtK': 5, 'G`rHpk': 4, 'G`K~A{': 4, 'GK]Sj[': 4, 'G{CWz[': 3, 'GQUax{': 5, 'G`N@x{': 3, 'GwCYx{': 4, 'G`ouX{': 4, 'GJaJ[{': 4, 'G`K~E{': 3, 'G`N@z{': 4, 'GJaKz{': 4, 'GwC[z{': 3, 'G`N@~{': 3, 'GJaJzw': 3, 'GTPLzw': 4, 'G`NDzw': 3, 'GJaJ~w': 3, 'GJaJz{': 3, 'GTPLz{': 4, 'G`NDz{': 3, 'GJaJ~{': 3, 'GwC^~w': 2, 'GwC^~{': 2, 'GWU[zk': 4, 'GIi[zk': 4, 'GpOxy{': 4, 'GoTXx{': 4, 'GSXYx{': 4, 'G`Ltu[': 4, 'GpOx}{': 4, 'GWU[z{': 4, 'GHq[z{': 4, 'Gagxz{': 4, 'G`gzm{': 4, 'GoKyz{': 4, 'GcKz^{': 4, 'GQSxx{': 4, 'GKdXx{': 4, 'G`hYx{': 4, 'GDXh}{': 4, 'GKcxz{': 4, 'GQSxz{': 4, 'GKWx}{': 4, 'GaSx|{': 4, 'GQSx~{': 4, 'GKXX{{': 5, 'G`X[x{': 4, 'GHeY~[': 4, 'GIM[z{': 4, 'GQS{z{': 4, 'G`dX~[': 4, 'GIM[~{': 4, 'GDtj^k': 4, 'GEXl|{': 4, 'GEXj|{': 4, 'GEXl~{': 4, 'GJeX~[': 4, 'GBij}{': 4, 'GKczz{': 4, 'GQS|z{': 4, 'GQMj}{': 4, 'GKcz~{': 4, 'GRTX~[': 4, 'GQSzz{': 4, 'GQSz~{': 4, 'GKth~k': 4, 'G`S~n[': 4, 'GKTj|{': 4, 'GKX\\|{': 4, 'GJ_~]{': 4, 'GKX\\~{': 4, 'Gbcx~[': 4, 'GaK|~[': 4, 'GIeZ|{': 4, 'GaK|z{': 4, 'G`Ll}{': 4, 'GcKzz{': 4, 'GcKz~{': 4, 'GQS~~w': 4, 'GQS~~{': 4, 'G?\\}dc': 4, 'GBbLZo': 5, 'GBJM\\o': 4, 'GGT{tc': 5, 'GYSW|K': 4, 'GQSw~C': 4, 'GR`LYw': 5, 'GJaJ[w': 4, 'GKJKzo': 5, 'GNOk[[': 4, 'GQ\\O|K': 5, 'GG\\ssk': 4, 'GwCYxw': 4, 'GK`kzo': 4, 'GJEM\\W': 5, 'GEubH{': 4, 'GDXm`{': 4, 'GcsrH{': 5, 'GkcZH{': 4, 'GKd^@{': 4, 'GTPip{': 5, 'G`LuP{': 4, 'GMeJH{': 5, 'GeopX{': 4, 'GwEYp{': 4, 'GDleJ{': 4, 'GB^DJ{': 4, 'GSlaj{': 5, 'GpK]J{': 4, 'GB^DN{': 4, 'GJYJk{': 4, 'GKX\\tk': 5, 'GYS~C{': 4, 'GQSx~K': 4, 'GKdX~K': 4, 'G`Kzm[': 4, 'GQhZtk': 5, 'GJNE\\{': 4, 'GTO}Z{': 4, 'GJ`kz{': 4, 'GTQiz{': 5, 'G`MuZ{': 4, 'GhNA|{': 4, 'GJ`k~{': 4, 'GTlai[': 5, 'G@\\~Ec': 4, 'G`NLrk': 4, 'GQh\\rk': 5, 'GJaZZs': 4, 'GJ^DK{': 4, 'GKYY|k': 5, 'G`oxzk': 4, 'GwEYx{': 4, 'GTOzY{': 5, 'GKeZj[': 4, 'GYUa|{': 4, 'G`qpz{': 4, 'GQUtZ{': 5, 'GKdrZ{': 4, 'GKdr^{': 4, 'GDlZNC': 4, 'G_mzbc': 3, 'GD]rUK': 5, 'G`K~eW': 3, 'GJnEH{': 3, 'Gb]eH{': 4, 'GTRHzs': 4, 'G`n@zk': 4, 'GtPHx{': 3, 'GRhP}[': 5, 'G`N`}s': 3, 'GMudJ{': 3, 'GjaHz{': 3, 'GYUcz{': 4, 'GtPH~{': 3, 'GDlbm[': 5, 'GPUrY{': 5, 'GQUpz[': 5, 'GKdZl[': 5, 'GQK|Y{': 5, 'GDYr]{': 5, 'GTOz]{': 5, 'GQgyz{': 5, 'G`qXz{': 5, 'GQMi~{': 5, 'G`K~e[': 3, 'G`Kx}[': 3, 'G`rHx{': 3, 'GKY[zk': 4, 'G`K~M{': 3, 'G`K}Z{': 4, 'GKY[z{': 4, 'GwCx}{': 3, 'G`K}^{': 3, 'G`o~vg': 3, 'G`rp~s': 3, 'GwEZz{': 3, 'GJaZ~[': 4, 'G`oz~k': 4, 'G`o~vk': 3, 'GwEZ~{': 3, 'GK\\k~k': 4, 'GKYZz{': 4, 'GQh\\z{': 5, 'G`NLz{': 4, 'GKYZ~{': 4, 'G`o~~w': 3, 'G`o~~{': 3, 'GcKxz[': 4, 'G`pXx{': 5, 'GQTXx{': 4, 'GcSxx{': 4, 'GgKx}{': 4, 'GQTX|{': 4, 'G`Wx}{': 4, 'GaKxz{': 4, 'GcKxz{': 4, 'GaKx~{': 4, 'GaKxx{': 4, 'G`Kx}{': 3, 'G`Kxz{': 3, 'G`Kx~{': 2, 'GeKx~[': 3, 'GKeZz{': 3, 'G`K~]{': 3, 'G`K}z{': 4, 'G`K}~{': 3, 'GhKx}{': 3, 'G`Kzz{': 3, 'G`K|z{': 3, 'G`Kz~{': 3, 'G`K~~w': 2, 'G`K~~{': 2, 'GJK}][': 3, 'GKczzw': 4, 'GKXzs{': 4, 'GKX\\|w': 4, 'GKeZzw': 3, 'GKdzvK': 3, 'GJNM\\{': 3, 'GJY[z{': 3, 'GThYz{': 4, 'G`\\u\\{': 3, 'GJY[~{': 3, 'G`lu^c': 3, 'GKxrk{': 3, 'GJdnK{': 3, 'GKd~fS': 3, 'GKMz]s': 4, 'G`Mzu[': 4, 'GKdznS': 4, 'G`K~]w': 3, 'GJ_~]w': 4, 'GTpuZ{': 3, 'GK^cz{': 3, 'GKZ\\r{': 4, 'GKfvR{': 3, 'G`Nmv{': 3, 'GNeZ^[': 3, 'GJe^^[': 3, 'GJeZ~[': 3, 'GJe^^{': 3, 'GKdzz{': 3, 'GKezz{': 4, 'GKfjz{': 3, 'GKdz~{': 3, 'GQT~t{': 4, 'GQUz~s': 4, 'GQTz|{': 4, 'G`N\\z{': 4, 'GQT|~{': 4, 'GKd~^s': 3, 'G`L~]{': 4, 'G`Nv]{': 3, 'G`Nm~{': 3, 'GKd~~{': 3, 'GJUl[{': 4, 'GTXiy{': 4, 'GMdr\\[': 4, 'GeK|Z[': 4, 'GRiiy{': 4, 'GQUxzs': 4, 'GQh\\zw': 5, 'GIeZ|w': 4, 'GeKxz[': 4, 'GJ`}\\s': 4, 'GeXh|{': 4, 'GMXk|{': 4, 'GLeZZ{': 4, 'GRT\\Z{': 4, 'GK\\ml{': 4, 'GdK}Z{': 4, 'GRT\\^{': 4, 'GLXi{{': 4, 'GkSxx{': 3, 'GQSzzw': 4, 'GcKzzw': 4, 'G`Kzzw': 3, 'GYTX|{': 3, 'GQTzt{': 4, 'G`Lzr{': 3, 'G`Lzt{': 3, 'G`Lzv{': 3, 'GqKx}[': 3, 'GbK|][': 4, 'GqSxx{': 3, 'Gakxzk': 4, 'G`K|zw': 3, 'GkKx}{': 3, 'G`Mzu{': 4, 'GpKyz{': 3, 'G`Mzv{': 3, 'GxKy}{': 3, 'GYT\\|{': 3, 'G`L|~s': 3, 'GhK}~{': 3, 'G`L~r{': 3, 'G`Lzz{': 3, 'G`Mzz{': 3, 'G`Lz~{': 3, 'G`Mz~{': 3, 'G`L~~{': 3, 'G`N~vs': 2, 'GKd~~w': 3, 'G`L~~w': 3, 'G`N~v{': 2, 'G`N~~{': 2, 'G{S~?{': 4, 'GTX^e[': 4, 'GTprY{': 4, 'GJdu\\[': 4, 'GJMk}[': 4, 'GNbLZ{': 4, 'GTX]Z{': 4, 'GJqkz{': 4, 'GJqk~{': 4, 'G`xt}w': 4, 'GMd|v[': 4, 'GQurz{': 4, 'GQlv]{': 4, 'GRUj}{': 4, 'GJfJ|{': 4, 'GJi^]{': 4, 'GRh^]{': 4, 'GQur~{': 4, 'GTlrY{': 4, 'GLlr]{': 4, 'GTXZz{': 4, 'GTX\\z{': 4, 'GTXZ~{': 4, 'GTX^~w': 4, 'GTX^~{': 4, 'GBl^NK': 4, 'GStrj[': 4, 'GD^evK': 4, 'GRK}][': 3, 'GMhq|[': 4, 'GEnfJ{': 3, 'GLNMZ{': 3, 'GUXkz{': 3, 'GMi^J{': 4, 'GRrH~{': 3, 'GbMlY{': 4, 'GqK|Y{': 4, 'GUXi|{': 4, 'Gkcxz{': 3, 'GqSxz{': 3, 'GqSx~{': 3, 'G{UrO{': 4, 'G`lvUk': 4, 'GRh^e[': 4, 'GMhr[{': 4, 'GRMi}[': 4, 'GMfdZ{': 4, 'G[X[z{': 4, 'GMjTZ{': 4, 'GLZKz{': 4, 'GRqi~{': 4, 'GZeY~[': 3, 'GYeZz{': 3, 'GRrLz{': 3, 'GqSz|{': 3, 'GYUZ|{': 3, 'GYeZ~{': 3, 'GlKz]{': 3, 'GpLZz{': 3, 'G`ltz{': 3, 'GpLZ~{': 3, 'G`zTzw': 4, 'GJf\\v[': 4, 'GRp^\\{': 4, 'GRVJ|{': 4, 'GKurz{': 4, 'G`lv]{': 4, 'GMiZ~{': 4, 'G`lv~w': 3, 'G`lv~{': 3, 'GQ\\{~c': 4, 'GJ][~K': 3, 'GD\\z^c': 4, 'GJ]]l[': 4, 'GYT{|s': 4, 'G`Lz~o': 3, 'GR\\^L{': 4, 'G`\\~d{': 3, 'GJ^cz{': 3, 'GJ^c~{': 3, 'GT\\~e[': 3, 'Gj]u\\{': 3, 'Gdnbz{': 3, 'GjNL~{': 3, 'GLnb}{': 3, 'GTpzz{': 3, 'GJq|~{': 3, 'GJq~~{': 3, 'GJyZ~k': 3, 'GJq|z{': 3, 'GJ]^n[': 3, 'GJp|~{': 3, 'GJpz|{': 3, 'GK\\zz{': 3, 'GQlzz{': 4, 'G`lzz{': 3, 'GK\\z~{': 3, 'GTVjz{': 4, 'GRUz~[': 4, 'GQmzz{': 4, 'GQlz~{': 4, 'G`lz~k': 3, 'G`]~j{': 3, 'G`mzz{': 3, 'G`lz~{': 3, 'GK\\~~{': 3, 'GLp^\\w': 4, 'GRrLzw': 4, 'GQ\\}tk': 4, 'GH^U|w': 4, 'GJi^]w': 4, 'GD]zvK': 4, 'GQT~tw': 4, 'GH]]~g': 4, 'GQNm~o': 4, 'GqN\\r{': 4, 'GRvLj{': 4, 'GT\\mj{': 4, 'GQu~b{': 4, 'GRlu^{': 4, 'GLZ\\~s': 4, 'GJj]|{': 4, 'GQl~vk': 4, 'GLY}~{': 4, 'GQl~~{': 4, 'GySx{{': 3, 'GNZL[{': 4, 'Griiy{': 3, 'GrTX|[': 3, 'GRh^]w': 4, 'GQ[}~g': 4, 'G`Mz~o': 3, 'G`Nm~o': 3, 'GyM[z{': 3, 'GZq[z{': 3, 'G`l~b{': 3, 'GNqkz{': 4, 'G`l~f{': 3, 'G`nr~s': 3, 'GYV\\|{': 3, 'G`l~vk': 3, 'G`]~n{': 3, 'GK^\\~k': 4, 'GKnZ~k': 4, 'G`tz|{': 4, 'GK\\}|{': 4, 'G`z\\z{': 4, 'G`uz~{': 4, 'G`l~~{': 3, 'GK|~nk': 3, 'GJfn~w': 3, 'GK\\~~w': 3, 'GQl~~w': 4, 'G`l~~w': 3, 'GK^~v{': 3, 'GK^~~{': 3, 'Gf~fH{': 2, 'G`~vvk': 3, 'G{dzz{': 2, 'G`~vn{': 2, 'G`~~vk': 2, 'G`~v~{': 2, 'G`~~~{': 2, 'GB]^nW': 3, 'G@\\~vg': 3, 'GD\\zvK': 3, 'G`lrzw': 3, 'GR\\s}[': 3, 'GY\\s{{': 3, 'GJY]|w': 4, 'GB^vT{': 3, 'GB^vR{': 3, 'GR\\u\\{': 3, 'GdXzt{': 3, 'GB^vV{': 3, 'GRo~]w': 3, 'GRp^\\w': 4, 'Grqix{': 3, 'GP\\}uk': 3, 'G`mzrk': 3, 'GYu\\j{': 3, 'GdlrZ{': 3, 'GMutZ{': 3, 'Gdlr^{': 3, 'GS\\~vg': 3, 'GJ]^nW': 3, 'GRl~e[': 3, 'Gb^vT{': 3, 'GJzT|{': 3, 'GJzT~{': 3, 'GJzR|{': 3, 'GMhzz{': 3, 'GRqzz{': 3, 'GpUzz{': 3, 'GMhz~{': 3, 'GL^d}{': 3, 'G[V\\z{': 3, 'GRqz~{': 3, 'Gdlr~[': 3, 'GMh}|{': 3, 'GdYz~{': 3, 'GMh~~{': 3, 'GqN~vs': 3, 'GMh~~w': 3, 'GqN~v{': 3, 'GqN~~{': 3, 'GB^v^o': 3, 'GQl~vg': 4, 'GtlrY{': 3, 'GJz^d{': 3, 'GMnbz{': 3, 'GRzTz{': 3, 'Gd^dz{': 3, 'GtX\\z{': 3, 'GMnb~{': 3, 'Gro~~w': 3, 'Gro~~{': 3, 'GD^v^o': 3, 'G`l~vg': 3, 'Gd]zvK': 3, 'GMnvR{': 3, 'GrzP~{': 3, 'Grz^`{': 3, 'Gql~vk': 3, 'GLx}~k': 3, 'GMl~n[': 3, 'Gd^v^{': 3, 'GL\\~]{': 3, 'GRl~]{': 3, 'GL^m~{': 3, 'GRz^~{': 3, 'GJnv]{': 3, 'GJm~]{': 3, 'GJ^m|{': 3, 'GJz\\~{': 3, 'GJ\\}|{': 3, 'GJ^\\~{': 3, 'GJu~~{': 3, 'GNzm|{': 3, 'GRz^~w': 3, 'GJu~~w': 3, 'GMn~v{': 3, 'GMn~~{': 3, 'Grx}|{': 3, 'Gr\\}|{': 3, 'G]uz~{': 3, 'GR~v~{': 3, 'GR~~~{': 3, 'G\\pz}{': 3, 'Gqmzz{': 3, 'Gbmz~[': 3, 'GMmz~[': 3, 'G[\\}~{': 3, 'GJv\\|{': 3, 'Gdlz~{': 3, 'GMmzz{': 3, 'GMmz~{': 3, 'GR^^~{': 3, 'GT\\~~{': 3, 'GZ^]|{': 3, 'GR^^~w': 3, 'GT\\~~w': 3, 'GR^~v{': 3, 'GR^~~{': 3, 'G[\\z}{': 3, 'Gdlzz{': 3, 'GUlzz{': 3, 'GR\\}~{': 3, 'GTlzz{': 3, 'GT\\z~{': 3, 'GR\\~~{': 3, 'GR\\z}{': 3, 'GT\\zz{': 3, 'GR\\z~{': 3, 'GR\\zz{': 3, 'GJ\\z~{': 2, 'GJ\\~~{': 2, 'GJ^~~{': 2, 'GJ~~~{': 2, 'GN~~~{': 2, 'GR\\~~w': 3, 'GJ\\~~w': 2, 'Gt\\zz{': 2, 'GJ^~v{': 2, 'Gtlzz{': 2, 'Gt\\z~{': 2, 'GJ~v~{': 2, 'Gt\\~~{': 2, 'GNz~~{': 2, 'GR~~vk': 3, 'GJ~~vk': 2, 'Gt\\~~w': 2, 'GN~v^{': 2, 'G~z\\z{': 2, 'G}l~~{': 2, 'Gr~~~{': 2, 'G^~~~{': 2, 'G~~~~{': 1}

def multi_sshow_zfs(all_graphs,each_row=0,text=None,final_figsize=None):
    """
    Input:
        all_graphs: a list of graph strings
        each_row: how many graphs displayed on each row, default is 0 (all)
        text: a string shown on the output picture, default is to show the strings of all_graphs
        final_figsize: the figsize of the output picture, default is [12,2]
    Output:
        a picture of all graphs in all_graphs in a row, plus text as the title.
    """
    if each_row==0:
        pic=Graph(0).plot();
        shift=0;
        gap=1;
        for stg in all_graphs:
            g=Graph(stg);
            draft=g.plot(save_pos=True);
            xy_range=draft.get_axes_range();
            local_shift=-xy_range["xmin"];
            x_range=xy_range["xmax"]-xy_range["xmin"];
            gpos=g.get_pos();
            for v in g.vertices():
                gpos[v][0]+=shift+local_shift;
            gpic=g.plot(figsize=[2,2],vertex_labels=False,vertex_size=50,pos=gpos,vertex_colors={'blue':list(find_gzfs(g))});
            pic+=gpic;
            shift+=x_range+gap;
            pic+=line([(shift-0.5*gap,-0.5),(shift-0.5*gap,0.5)],linestyle="--");
        pic.axes(False);
        if text==None:
            text="";
            for stg in all_graphs:
                g=Graph(stg)
                text+="Z(g)=";
                text+=str(find_gZ(g));
                text+=", "
                text+="Zhat(g)=";
                text+=str(find_EZ( g ))
                text+=",   "
        if final_figsize==None:
            final_figsize=[12,2];
        pic.show(figsize=final_figsize, title=text);
        
    if each_row>0:
        cache=[];
        period=0;
        for stg in all_graphs:
            cache.append(stg);
            period+=1;
            if period==each_row:
                multi_sshow_zfs(cache);
                cache=[];
                period=0;
        if cache!=[]:
            multi_sshow_zfs(cache)
            
def closed_nbr(g,v):
    nbrs=[]

    for i in g.neighbor_iterator(v):
        nbrs.append(i)
    nbrs.append(v)
    return set(nbrs)

def adj_twins(g):
    twins=[]
    for v in g.vertices():
        for w in g.vertices():
            if w>v:
                if closed_nbr(g,v)==closed_nbr(g,w): 
                        twins.append([v,w])
    return(twins) 

def non_adj_twins(g):
    twins=[]
    for v in g.vertices():
        for w in g.vertices():
            if w>v:
                if g.neighbors(v)==g.neighbors(w): #neighborhoods are open by default
                        twins.append([v,w])
    return(twins)

def twins_agree(g):
    if twinningM_equal_Z(g,max_null=True,adjacent=True)==twinningM_equal_Z(g,max_null=True,adjacent=False):
        return True
    else:
        return False
    
#In the diagonal analysis of a graph with a pair of adjacent twins, checks for a one or a two on the diagonal entry corresponding to them.
#Deletes one, finds the minrank of G-v.  Chooses the smallest one, computes minrank G since adding back v shouldn't change minrank
def twinningM_equal_Z(g,max_null=False,adjacent=True):
    k=1 #corresponds to default adjacent=True, check for this entry in diagonal analysis
    n=g.order() #save original size of graph
    orig_z=find_gZ(g) #find Z(g)
    good_vs=[] 
    if adjacent==False: #non adjacent twins
        k=0 
        for i in range(len(non_adj_twins(g))):
            v=non_adj_twins(g)[i][0]
            w=non_adj_twins(g)[i][1]
            g_min_v=deepcopy(g)
            g_min_v.delete_vertex(v) #need to check diagonal analysis on G-v. G-v and G-w are the same graph           
            if (diagonal_analysis(g_min_v)[w]==k or diagonal_analysis(g_min_v)[w]==2):  #check for valid diag entries to add v back with same minrank  
                good_vs.append(w)
    else:    
        for i in range(len(adj_twins(g))):
            v=adj_twins(g)[i][0]
            w=adj_twins(g)[i][1]
            g_min_v=deepcopy(g)
            g_min_v.delete_vertex(v)            
            if (diagonal_analysis(g_min_v)[w]==k or diagonal_analysis(g_min_v)[w]==2):    
                good_vs.append(w)
    good_vs= list(set(good_vs))  #delete repeats, don't think this is necessary with current code          
    mudict=[]
    for v in good_vs:
        gg=deepcopy(g)
        gg.delete_vertex(v)
        mudict.append(get_mr_from_list(gg))    #Get mr(G-v) from list
    if len(mudict)>0: #ie viable vertices to delete
        mr=min(mudict)
        M=n-mr #take max nullity of twin sets, add one for when v is added back
        if max_null==True:
            return M
        else:    
            if M==orig_z:  
                return True
            else:
                return False      
    else:
        return -1 #no twins or good_vs empty
##overwrite of previous find_mu(g), decreasing upper bound to the zero forcing number
def find_mu(g):
    """
    Try to find mu for a given graph, by low-value tests, such 
    as planarity.
    
    INPUT
    g: a graph
    
    OUTPUT
    mu, if the exact value is determined;
    (low_bound,up_bound), otherwise.
    """
    n=g.order();
    low_bound,up_bound=0,n;
    min_deg=n-1;
    max_deg=0;
    ## Get min/max_deg
    for i in g.vertices():
        deg=g.degree(i);
        if deg<min_deg:
            min_deg=deg;
        if deg>max_deg:
            max_deg=deg; 
    ## Decrease up_bound
    if min_deg==n-1:
        return n-1;
    up_bound=find_gZ(g);     
    ## This up_bound does not apply for K2,
    ## but doesn't change the result.
    ## Increase low_bound         
    if n==1:
        return 0;
    if g.is_forest():
        if max_deg<=2:
            return 1;
        return 2;                
    if g.is_circular_planar():
        return 2;
    if g.is_planar():
        return 3;
    low_bound=4;
    for p in PetersenFamily:
        if has_minor(g,p):
            low_bound=5;
    if low_bound==4:
        return 4;
    ## No idea now.
    up_bound=min(up_bound,mu_upper(g));
    if low_bound==up_bound:
        return low_bound;
    return (low_bound,up_bound);
## Need has_minor function and PetersenFamily list.
## Minor algorithm works slow.

def simplicial_vertices(g):
    simp_verts=[]
    for v in g.vertices():
        if g.is_clique(g.neighbors(v)):
            simp_verts.append(v)
    return simp_verts

def simplicial_vertex_minrank(g):
    V=simplicial_vertices(g)
    diag=diagonal_analysis(g)
    count=0
    if len(V)==0 or g.order()>8:
        return -1
    for v in V:
        #print v, diag
        if diag[v]==0:
            count+=1
            gg=g.delete_vertex(v)
            return get_mr_from_list(gg) 

def has_forbidden_minor_3_connected_m_equal_3( g , return_minor = False ):
    forb_minors_M_equal_3= [ 'Gl`HGs', 'FxVKg', 'E]~o', 'D~{', 'EFz_' ]     #[ Q3, Q3Ydelta, K222, K5, K33
    if g.vertex_connectivity()==3:
        for stg in forb_minors_M_equal_3:
            m=Graph(stg)
            if has_minor(g,m):
                if return_minor == True:
                    return m.graph6_string()
                return True
    else:
        return False    
    if count == 0:
        #print "no viable simplicial vertices"
        return -1

list_udt=['Gb\\ltg', 'Gb\\|tg', 'Gb\\ntg', 'Gb\\nvg', 'Gb\\ntk', 'Gb\\nvk',
'Gb\\lvg', 'GbTnvk', 'GbTlvg', 'GbTnvg', 'G~S{|K', 'Gz[k~[', 'GzSk|k',
'Gr[m^[', 'Gz[m^[', 'GrSm^[', 'Gvr|Rw', 'Gvz|Rw', 'Gfr|Rw', 'G~X[\\s',
'G~x[\\s', 'G~Z[\\s', 'G~z[\\s', 'G~Z[\\{', 'G~z[\\{', 'G~X]\\s',
'Gzx[\\c', 'G~x[\\c', 'G~z[\\c', 'Gzx[|c', 'G~x[|c', 'GzX[\\k',
'GzX{\\k', 'GrX[\\k', 'GrZ[\\k', 'G~xX[s', 'G~XX{s', 'Grx\\]c',
'Gvx\\]c', 'Grx^]c', 'Grx\\}c', 'Gvx\\}c', 'Gv|\\}c', 'Grx^}c',
'Grx\\]k', 'GzX][k', 'GzX]]k']

def check_isomorphisms(G, new_li):
    for H in new_li:
        if G.is_isomorphic(H):
            return True
    return False
    
def remove_isomorphisms(li):
    if li == []:
        return li
    new_li = [li[0]]
    for G in li:
        if check_isomorphisms(G, new_li) is True:
            continue
        else:
            new_li.append(G)

    return new_li   
    
def max_degree_subgraphs(G):
    g=Graph(G)
    subgr=[]
    for v in g.vertices():
        #print 'v=', v
        #print 'v deg=', g.degree(v)
        gg=deepcopy(g)
        if g.degree(v) == max(g.degree_sequence()):
            #print 'v=',v
            #print 'g degree sequence',g.degree_sequence()
            #print 'v degree',gg.degree(v)
            gg.delete_vertex(v)
            #print 'gg degree sequence',gg.degree_sequence()
            subgr.append(gg)
    return subgr

G={}

G[721]=Matrix([[-1, 1, 0, 0, 1,0,1],[1,-1,1,0,0,1,0],[0,1,-1,1,0,-1,0],[0,0,1,0,1,1,1],           [1,0,0,1,0,0,0],[0,1,-1,1,0,-1,0],[1,0,0,1,0,0,0]])

G[801]=Matrix([[0, 1, 1, 0, -1, -1, -1],[1, 1, 1, 1, 0, 0, 0],[1, 1, 1, 1, 0, 0, 
0],[0, 1, 1, 0, -1, -1, -1],           [-1, 0, 0, -1, 0, 0, 0],[-1, 0, 0,-1, 
0, 0, 0],[-1, 0, 0,-1, 0, 0, 0]])

G[812]=Matrix([[0,1,1,0,0,0,0],[1,0,0,1,1,0,1],[1,0,0,1,1,0,1],[0,1,1,1,1,1,0],
[0,1,1,1,1,1,0],[0,0,0,1,1,1,0],[0,1,1,0,0,0,0]])

G[831]=Matrix([[0,-1,1,0,0,0,0],[-1,0,1,0,0,1,-1],[1,1,-1,1,1,0,1],
[0,0,1,1,1,1,0],[0,0,1,1,1,1,0],[0,1,0,1,1,1,0],[0,-1,1,0,0,0,0]])

G[832]=Matrix([[-1,-1,-1,0,0,0,-1],[-1,0,-2,-1,0,-1,-1],[-1,-2,-1,0,-1,0,-1],[0,-
1,0,0,-1,0,0],[0,0,-1,-1,-1,-1,0],[0,-1,0,0,-1,0,0],[-1,-1,-1,0,0,0,-1]])

G[846]=matrix([[0, -2, 0, 0, 1, 0, 0], 
[-2, 0, 1, 0, 0, 1, 1],
[0, 1,1/2, 1, 0, 1, 0],
[0, 0, 1, 2, 1, 2, 0],
[1, 0, 0, 1, 1/2,1/2, -1/2],
[0, 1, 1, 2, 1/2, 2, 0],
[0, 1, 0, 0, -1/2, 0, 0]])

G[863]=Matrix([[-1,1,1,0,0,0,-1],[1,-1,0,1,0,1,1],[1,0,0,1,1,0,1],
[0,1,1,1,1,0,0],[0,0,1,1,0,1,0],[0,1,0,0,1,-1,0],[-1,1,1,0,0,0,-1]])

G[873]=Matrix([[1,-1,-1,0,0,0,1],[-1,0,0,-1,0,-1,-1],[-1,0,0,-1,0,-1,-1],[0,-1,-
1,0,-1,0,0],[0,0,0,-1,1,-1,0],[0,-1,-1,0,-1,0,0],[1,-1,-1,0,0,0,1]])

G[878]=Matrix([[-1, 1, 0, 0, 1,0,-1],[1,-1,1,0,0,1,1],[0,1,-1,1,0,-1,0],[0,0,1,0,1,1,0],           [1,0,0,1,0,0,1],[0,1,-1,1,0,-1,0],[-1, 1, 0, 0, 1,0,-1]])

G[913]=Matrix([[1,1,1,1,0,0,0],[1,1,1,1,0,0,0],[1,1,2,2,1,1,1],[1,1,2,2,1,1,1],[0,0,1,1,0,0,0],[0,0,1,1,0,0,0],[0,0,1,1,0,0,0]])

G[918]=Matrix([[0,-1,-1,0,0,0,0],[-1,-1,-1,-1,-1,0,-1],[-1,-1,-1,-1,-1,0,-1],[0,-1,-1,-1,-1,1,0],[0,-1,-1,-1,-1,1,0],[0,0,0,1,1,-1,0],[0,-1,-1,0,0,0,0]])

G[924]=Matrix([[0,0,1,1,0,0,0],[0,0,1,1,0,0,0],[1,1,1,1,1,0,0],[1,1,1,2,2,1,1],
[0,0,1,2,1,1,1],[0,0,0,1,1,1,1],[0,0,0,1,1,1,1]])

G[932]=Matrix([[0,-1,-1,0,0,0,0],[-1,-2,-1,2,-1,0,-1],[-1,-1,-1,1,0,-1,-1],
[0,2,1,-1,1,-1,0],[0,-1,0,1,-1,1,0],[0,0,-1,-1,1,-1,0],[0,-1,-1,0,0,0,0]])

G[944]=Matrix([[1,1,1,0,0,0,1],[1,1,2,0,1,1,2],[1,2,1,1,0,0,1],[0,0,1,0,1,1,1],
[0,1,0,1,0,0,0],[0,1,0,1,0,0,0],[1,2,1,1,0,0,1]])

G[953]=Matrix([[-2,1,0,1,0,0,0],[1,0,1/2,0,1,1/2,1/2],
[0,1/2,1,1,1,0,0],[1,0,1,1/2,1,0,0],
[0,1,1,1,2,1,1],[0,1/2,0,0,1,1,1],[0,1/2,0,0,1,1,1]])

G[956]=Matrix([[1,1,0,1,1,1,1],[1,0,1,0,0,1,0],[0,1,0,1,0,0,0],[1,0,1,0,0,1,0],
[1,0,0,0,1,1,1],[1,1,0,1,1,1,1],[1,0,0,0,1,1,1]])

G[958]=Matrix([[0,1,1,-2,1,1,0],[1,1,1,0,0,0,1],[1,1,1,0,0,0,1],[-2,0,0,-2,0,0,-
2],[1,0,0,0,1,1,1],[1,0,0,0,1,1,1],[0,1,1,-2,1,1,0]])

G[970]=Matrix([[1,1,1,0,0,0,0],[1,2,2,1,1,0,0],[1,2,1,1,0,-1,-1],[0,1,1,1,1,0,0],[0,1,0,1,0,-1,-1],[0,0,-1,0,-1,-1,-1],[0,0,-1,0,-1,-1,-1]])

G[990]=Matrix([[1/8,1/2,0,1/2,0,0,0],[1/2,0,2,1,1,0,0],[0,2,-1,1,0,1,1],[1/2,1,1,3/2,1/2,0,0],[0,1,0,1/2,1/2,1,1],[0,0,1,0,1,1,1],[0,0,1,0,1,1,1]])

G[995]=Matrix([[1,1,0,1,1,0,0],[1,1,1,0,0,1,1],[0,1,-1,1,2,0,0],[1,0,1,0,-1,0,0],[1,0,2,-1,-2,1,1],[0,1,0,0,1,1,1],[0,1,0,0,1,1,1]])

G[996]=Matrix([[1,0,1,0,1,0,1],[0,2,1,1,0,2,0],[1,1,1,0,2,1,1],[0,1,0,0,1,1,0],[1,0,2,1,-1,0,1],[0,2,1,1,0,2,0],[1,0,1,0,1,0,1]])

G[1002]=Matrix([[1,0,1,1,0,0,1],[0,0,1,1,-1,-1,0],[1,1,1,0,0,-1,1],[1,1,0,-1,1,0,1],[0,-1,0,1,0,1,0],[0,-1,-1,0,1,2,0],[1,0,1,1,0,0,1]])

G[1005]=matrix(
[(1, 0, 0, 0, 1, 1, 1), 
(0, 1, 0, 1, 0, -1, 1), 
(0, 0, 1, 1, 1, 0, -1),
(0, 1, 1, 2, 1,-1, 0), 
(1, 0, 1,1, 2, 1, 0), 
(1,-1, 0, -1, 1, 2, 0), 
(1,1, -1, 0, 0, 0, 3)])

G[1028]=Matrix([[1,0,2,-1,1,1,0],[0,0,1,0,1,0,0],[2,1,4,-1,2,2,1],[-1,0,-1,1,0,-1,0],[1,1,2,0,1,1,1],[1,0,2,-1,1,1,0],[0,0,1,0,1,0,0]])

G[1060]=Matrix([[2,-1,-1,0,1,1,0],[-1,2,1,1,1,0,1],[-1,1,1,0,0,0,1],[0,1,0,1,1,0,0],[1,1,0,1,2,1,1],[1,0,0,0,1,1,1],[0,1,1,0,1,1,2]])

G[1075]=Matrix([[0,-1,2,1,2,0,0],[-1,0,1,0,0,1,-1],[2,1,0,1,0,0,2],[1,0,1,1,1,0,1],[2,0,0,1,1,-1,2],[0,1,0,0,-1,1,0],[0,-1,2,1,2,0,0]])


G[1077]=Matrix([[0,0,1,1,1,0,0],[0,1,0,-1,-1,0,1],[1,0,1,1,0,1,0],[1,-1,1,2,1,1,-1],[1,-1,0,1,0,1,-1],[0,0,1,1,1,0,0],[0,1,0,-1,-1,0,1]])

G[1087]=Matrix([[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,-1,0,1,1],[1,0,-1,-1,-1,0,1],[1,1,0,-1,0,1,1],[0,1,1,0,1,1,0],[0,0,1,1,1,0,0]])

G[1095]=matrix(
[(2,1,0,0,1,-1,-1), 
(1,2,1,0,0,-1,2), 
(0,1,1,1,0,0,2),
(0,0,1,3,1,1,1),
(1,0,0,1,1,0,-1),
(-1,-1,0,1,0,1,0),
(-1,2,2,1,-1,0,5)])

G[1099]=Matrix([[1,0,1,0,1,0,1],[0,2,1,1,0,2,0],[1,1,1,0,2,1,2],[0,1,0,0,1,1,1],[1,0,2,1,-1,0,-1],[0,2,1,1,0,2,0],[1,0,2,1,-1,0,-1]])

G[1104]=matrix(
[(-1,2,2,3,0,0,0), 
(2,-1,2,0,3,0,3), 
(2,2,-1,0,0,3,-3),
(3,0,0,-1,2,2,0), 
(0,3,0,2,-1,2,-3), 
(0,0,3,2,2,-1,3), 
(0,3,-3,0,-3,3,-6)])

G[1146]=matrix([[-1,1,0,0,-1,0,-3],[1,-2,1,0,1,-1,4],
[0,1,-2,1,1,1,-4],[0,0,1,-1,-1,0,3],[-1,1,1,-1,-2,0,0],[0,-1,1,0,0,-1,1],[-3,4,-4,3,0,1,-19]])


G[1167]=Matrix([[0,1,0,0,1,2,1],[1,-1,1,0,0,-1,-1],[0,1,-1,1,0,1,2],[0,0,1,-
1,1,1,-1],[1,0,0,1,0,0,1],[2,-1,1,1,0,-1,0],[1,-1,2,-1,1,0,-2]])

G[1205]=matrix(	
[(3/5, 1/10, -1/2,0,1,1,0), 
(1/10, 3/5, 1/2,1,0,1,0), 
(-1/2, 1/2, 1,1,-1,0,0),
(0, 1, 1,3, 1, 1,3),
(1, 0, -1,1, 3, 1,3),
(1, 1, 0,1, 1, 3,-1),
(0,0,0,3,3,-1,7)])



G[1212]=Matrix([(0, 4, -2, 3, 2, 1, 0), (4, -1, 1, 0, 0, 1, 4), (-2, 1,
-1, 1, 0, 0, -2), (3, 0, 1, -1, 1, 0, 3), (2, 0, 0, 1, 0, 1, 2), (1,
1, 0, 0, 1, 0, 1), (0, 4, -2, 3, 2, 1, 0)])

def subgraph_finder(h,llist):
    container=[]
    for i in range(len(llist)):
            g=Graph(list_udt[i])
            if g.subgraph_search_count(h,induced=True)>0:
                #print i
                container.append(i)
    return container 
    
def convert_to_simple_graph(mat):
    m=deepcopy(mat)
    for i in range(len(m[0])):
        for j in range(len(m[0])):
            if not m[i,j]==0:
                m[i,j]=1
        m[i,i]=0                
    return Graph(m)    
    
def missing_neighbors(g, v):
    V=g.vertices()
    for a in g.neighbors(v):
        V.remove(a)
    V.remove(v)    
    return V
    
def determine_P(g, h, deleted_vertex):
    # g a graph of order 8
    # h an induced subgraph of order 7 of g
    n=g.order()
    perms=[]
    m1=g.adjacency_matrix()
    m1=m1.delete_rows([deleted_vertex])
    m1=m1.delete_columns([deleted_vertex])
    #print "m1=",m1
    m2=h.adjacency_matrix()
    #hh=m2.insert_row(n-1,zero_vector(n-1))
    #print hh
    #ii=identity_matrix(n)
    #print ii
    #m2=hh.transpose().insert_row(n-1,ii[n-1]).transpose()
    #print "m2=",m2
    #m1=matrix([[0,3,0],[3,0,1],[0,1,0]])
    #m2=matrix([[0,1,0],[1,0,3],[0,3,0]])
    for p in Permutations([1..n-1]):
        perms.append(p.to_matrix())
    for i in range(len(perms)):
        P=perms[i]
        #print P.transpose()*m1*P
        if P*m1*P.transpose()==m2:
            #print deleted_vertex
            P=P.dense_matrix()
            
            P=P.insert_row(7,zero_vector(n-1))
           
            ii=identity_matrix(n)
            #print "ii[7]=",ii[7]
            
            P=P.transpose().insert_row(deleted_vertex,ii[7]).transpose()
            
            #print "m2=",m2
            #m1=matrix([[0,3,0],[3,0,1],[0,1,0]])
            #m2=matrix([[0,1,0],[1,0,3],[0,3,0]])
            return P  
    return False   
    
     

def lift_minrank_matrix( g , a ,null_vec=vector([1,1,1,1,1,1,1]),override=False):
    #g a graph
    #a the index from atlas of graphs for which g has induced subgraph isomorphic to G[a]
    GG = deepcopy(G[a])
    h=convert_to_simple_graph(GG)
    #g=Graph(list_udt[15])
    #g.show()
    #print g.vertices()
    deleted_vertex=g.vertices()
    if g.subgraph_search(h,induced=True).vertices()==None:
        return False
    for v in g.subgraph_search(h,induced=True).vertices():
        deleted_vertex.remove(v)
    #print "deleted-vertex",deleted_vertex
    m=deepcopy(GG)
    null_list=[]
    #for w in [2]:
    P=determine_P(g,h,deleted_vertex[0]).transpose()
    #p=Permutation(P)
    #if missing_neighbors(g, deleted_vertex[0])==[]:
        #print "dominating vertex"
    for w in missing_neighbors(g, deleted_vertex[0]):
        #print "missing neighbor",w
        #if return_perm(w,P.transpose()) ==7:
            #print "error to figure out"
        if return_perm(w,P.transpose()) !=7:
            null_list.append(list(m[return_perm(w,P.transpose())]))
    kern=matrix(null_list).right_kernel_matrix()
    v=sum(kern.rows())
    if null_list==[] or override==True:
        #print "empty null list"
        v=null_vec
    #print v
    w=v*GG
    list(w*matrix(v).transpose())[0]
    ww=list(w)
    ww.insert(7,list(w*matrix(v).transpose())[0])
    G2=GG.insert_row(7,w)
    #print "parent=",G2.parent()
    G3=G2.transpose().insert_row(7,ww).transpose()
    #print "G3=",G3
    #g.show()
    #g.delete_vertex(deleted_vertex[0])
    #g.show()
    #print "P=",P

    return P*G3*P.transpose() 
    #return G3
def lift_minrank_matrix_M( g , M ,null_vec=vector([1,1,1,1,1,1,1]),override=False):
    #g a graph
    #M a minrank matrix for an induced subgraph of G
    GG = deepcopy(M)
    h=convert_to_simple_graph(GG)
    n=g.order()
    deleted_vertex=g.vertices()
    if g.subgraph_search_count(h,induced=True)==0:
        return False
    if g.subgraph_search(h,induced=True).vertices()==None:
        return False
    for v in g.subgraph_search(h,induced=True).vertices():
        deleted_vertex.remove(v)
    #print "deleted-vertex",deleted_vertex
    m=deepcopy(GG)
    null_list=[]
    #for w in [2]:
    P=determine_P(g,h,deleted_vertex[0]).transpose()
    #print "P=",P
    #p=Permutation(P)
    if missing_neighbors(g, deleted_vertex[0])==[]:
        #print "dominating vertex"
    for w in missing_neighbors(g, deleted_vertex[0]):
        #print "missing neighbor",w
        #if return_perm(w,P.transpose()) ==7:
            #print "error to figure out"
        if return_perm(w,P.transpose()) !=7:
            null_list.append(list(m[return_perm(w,P.transpose())]))
    kern=matrix(null_list).right_kernel_matrix()
    #print kern
    v=sum(kern.rows())
    if null_list==[] or override==True:
        #print "empty null list"
        v=null_vec
    #print v
    w=v*GG
    #print w
    list(w*matrix(v).transpose())[0]
    ww=list(w)
    ww.insert(n,list(w*matrix(v).transpose())[0])
    G2=GG.insert_row(n-1,w)
    #print "parent=",G2.parent()
    G3=G2.transpose().insert_row(n-1,ww).transpose()
    #print "G3=",G3
    #g.show()
    #g.delete_vertex(deleted_vertex[0])
    #g.show()
    #print "P=",P

    return P*G3*P.transpose() 
    #return G3
    
    
def check_in_SG(g,A,prnt=False):
    n=g.order()
    m1=convert_to_simple_matrix(A)
    #print "m1=",m1
    m2=g.adjacency_matrix()
    #print "m2=",m2
    if prnt ==True:
        print(m1-m2)
    if m1-m2==matrix(n,n):
        return True
    return False
    
def return_perm(v,p):
    n=len(p[0])
    vec= [ 0 for k in range(n-1)]
    vec.insert(v,1)
    image= p*vector(vec)
    #return image
    #image=vector(image)
    for i in range(n):
        #print i
        if image[i]==1:
            return i
def convert_to_simple_matrix(mat):
    m=deepcopy(mat)
    for i in range(len(m[0])):
        for j in range(len(m[0])):
            if not m[i,j]==0:
                m[i,j]=1
        m[i,i]=0            
    return m   

def two_sep_minrank(g):
    if g.vertex_connectivity() == 2:
        #print 'G:'
        #g.plot().show(figsize=(2,2))
        L=g.vertex_connectivity(sets=True)
        # construction G1, G2 then computing mr
        G=g.copy()
        G1=g.copy()
        G2=g.copy()
        G1.delete_vertices(L[2][1])
        G2.delete_vertices(L[2][0])
        if L[1][1] in G.neighbors(L[1][0]):
            G1.delete_edge(L[1][1],L[1][0])
        #print 'r1 = ',L[1][0] 
        #print 'r2 = ',L[1][1]
        #print '-------------------------------------------'
        #print 
        #print 'G1:'
        #G1.plot().show(figsize=(2,2))
        mrG1 = minrank_bounds(G1)[0]
        #print 'mr(G1) = ', mrG1
        #print '-------------------------------------------'
        #print
        #print 'G2:'
        #G2.plot().show(figsize=(2,2))
        mrG2 =  minrank_bounds(G2)[0]
        #print 'mr(G2) = ', mrG2

        #constructing H1, H2 then computing mr
        H1=G1.copy()
        H2=G2.copy()
        H2.allow_multiple_edges(True)
        H1.add_edge(L[1][1],L[1][0])
        H2.add_edge(L[1][1],L[1][0])
        #print '-------------------------------------------'
        #print 
        #print 'H1:'
        #H1.plot().show(figsize=(2,2))
        mrH1 = minrank_bounds(H1)[0]
        #print 'mr(H1) = ', mrH1
        #print '-------------------------------------------'
        #print 
        #print 'H2:'
        #H2.plot().show(figsize=(2,2))
        if H2.has_multiple_edges() == True:
            aH2=H2.copy()
            bH2=H2.copy()
            aH2.delete_edge(aH2.multiple_edges()[0])
            #aH2.plot().show()
            bedge=bH2.multiple_edges()[0]
            bH2.delete_edge(bedge)
            bH2.delete_edge(bedge)
            #bH2.plot().show()
            mrH2=min(minrank_bounds(aH2)[0],minrank_bounds(bH2)[0])
        else:
            mrH2=minrank_bounds(H2)[0]
        #print 'mr(H2) = ',mrH2

        #constructing G1/r1r2, G2/r1r2 then computing mr
        G1r1r2 = G1.copy()
        G2r1r2 = G2.copy()
        G1r1r2.allow_multiple_edges(True)
        G2r1r2.allow_multiple_edges(True)
        G1r1r2.merge_vertices(L[1])
        #print '-------------------------------------------'
        #print
        #print 'G1/r1r2:'
        #G1r1r2.plot().show(figsize=(2,2))

        if G1r1r2.has_multiple_edges() == True:
            mG1r1r2=G1r1r2.copy()
            mG1r1r2.allow_multiple_edges(False)
            M=set(G1r1r2.multiple_edges())
            S=Subsets(M)
            #print S.list()
            ML=[]
            k=len(S)
            for i in range(k):
                ML.append(mG1r1r2.edges())
            #print ML
            mrML=[]
            for i in range(k):
                g=Graph([G1r1r2.vertices(),list(set(ML[i]).difference(S[i]))])
                #g.show(figsize=(2,2))
                mrML.append(minrank_bounds(g)[0])
            #print mrML
            #print min(mrML)
            mrG1r1r2 = min(mrML)
        else:
            mrG1r1r2 = minrank_bounds(G1r1r2)[0]
        #print 'mr(G1/r1r2) = ', mrG1r1r2
        G2r1r2.merge_vertices(L[1])
        #print '-------------------------------------------'
        #print
        #print 'G2/r1r2:'
        #G2r1r2.plot().show(figsize=(2,2))
        if G2r1r2.has_multiple_edges() == True:
            mG2r1r2=G2r1r2.copy()
            mG2r1r2.allow_multiple_edges(False)
            M=set(G2r1r2.multiple_edges())
            S=Subsets(M)
            #print S.list()
            ML=[]
            k=len(S)
            for i in range(k):
                ML.append(mG2r1r2.edges())
            #print ML
            mrML=[]
            for i in range(k):
                g=Graph([G2r1r2.vertices(),list(set(ML[i]).difference(S[i]))])
                #g.show(figsize=(2,2))
                mrML.append(minrank_bounds(g)[0])
            #print mrML
            #print min(mrML)
            mrG2r1r2 = min(mrML)
        else:
            mrG2r1r2 = minrank_bounds(G2r1r2)[0]
        #print
        #print G2r1r2.multiple_edges()
        #print 'mr(G2/r1r2) = ', mrG2r1r2

        #constructing G1-r1, G2-r1 then computing mr
        G1minusr1 = G1.copy()
        G2minusr1 = G2.copy()
        G1minusr1.delete_vertex(L[1][0])
        #print '-------------------------------------------'
        #print
        #print 'G1-r1:'
        #G1minusr1.plot().show(figsize=(2,2))
        mrG1minusr1 = minrank_bounds(G1minusr1)[0]
        #print 'mr(G1-r1) = ',mrG1minusr1
        G2minusr1.delete_vertex(L[1][0])
        #print '-------------------------------------------'
        #print
        #print 'G2-r1:'
        #G2minusr1.plot().show(figsize=(2,2))
        mrG2minusr1 = minrank_bounds(G2minusr1)[0]
        #print 'mr(G2-r1) = ',mrG2minusr1

        #constructing G1-r2, G2-r2 then computing mr
        G1minusr2 = G1.copy()
        G2minusr2 = G2.copy()
        G1minusr2.delete_vertex(L[1][1])
        #print '-------------------------------------------'
        #print
        #print 'G1-r2:'
        #G1minusr2.plot().show(figsize=(2,2))
        mrG1minusr2 = minrank_bounds(G1minusr2)[0]
        #print 'mr(G1-r2) = ',mrG1minusr2
        G2minusr2.delete_vertex(L[1][1])
        #print '-------------------------------------------'
        #print
        #print 'G2-r2:'
        #G2minusr2.plot().show(figsize=(2,2))
        mrG2minusr2 = minrank_bounds(G2minusr2)[0]
        #print 'mr(G2-r2) = ',mrG2minusr2

        #constructing G1-R, G2-R then computing mr
        G1minusR = G1.copy()
        G2minusR = G2.copy()
        G1minusR.delete_vertices(L[1])
        #print '-------------------------------------------'
        #print 
        #print 'G1-R:'
        #G1minusR.plot().show(figsize=(2,2))
        mrG1minusR = minrank_bounds(G1minusR)[0]
        #print 'mr(G1-R) = ',mrG1minusR
        G2minusR.delete_vertices(L[1])
        #print '-------------------------------------------'
        #print
        #print 'G2-R:'
        #G2minusR.plot().show(figsize=(2,2))
        mrG2minusR = minrank_bounds(G2minusR)[0]
        mr=min(mrG1 + mrG2,mrH1 + mrH2,mrG1r1r2 + mrG2r1r2 + 2,mrG1minusr1 + mrG2minusr1 + 2,mrG1minusr2 + mrG2minusr2 + 2,mrG1minusR + mrG2minusR + 4)
        #print 'mr(G2-R) = ',mrG2minusR
        #print
        #print

        #computing 2-separation minimum rank formula a la van der Holst
        #print 'mr(G1)+mr(G2)             = ', mrG1 + mrG2
        #print 'mr(H1)+mr(H2)             = ', mrH1 + mrH2
        #print 'mr(G1/r1r2)+mr(G2/r1r2)+2 = ', mrG1r1r2 + mrG2r1r2 + 2
        #print 'mr(G1-r1)+mr(G2-r1)+2     = ', mrG1minusr1 + mrG2minusr1 + 2
        #print 'mr(G1-r2)+mr(G2-r2)+2     = ', mrG1minusr2 + mrG2minusr2 + 2
        #print 'mr(G1-R)+mr(G2-R)+4       = ', mrG1minusR + mrG2minusR + 4
        #print '---------------------------------------------'
        #print 'mr(G)                     = ', mr
    else:
        print('not 2-separable')
    return mr;

def flatten(l):
  out = []
  for item in l:
    if isinstance(item, (list, tuple)):
      out.extend(flatten(item))
    else:
      out.append(item)
  return out

#Input: a symmetric matrix A ( could also do combinatorially symmetric by slight alteration )
#Output: Graphs G' where A in S(G) can be lifted to by adding a vertex and where there exists a matrix in S(G') with the same rank
def Col_Supp_Lifts(A):
   
    #print 'rank = ', A.rank(), '\n'
    #print A, '\n'
    #n number of rows/columns in A
    n=len(list(A))
   
    #constructing the graph for A
    #print 'G(A) = '
    G=Graph([])
    G.add_vertices(range(n))
    for i in range(0,n):
        for j in range(i+1,n):
            if A[i][j] != 0:
                G.add_edge((i,j))
    #G.show()
   
    #print '===========================================================', '\n', 'Minimal support lifts for A ', '\n'

    #requires sage matroid package, sage.matroids.advanced import *
    kerA=Matrix(A.kernel().basis())

    #Computing matroid data for the null space of the null space

    M=Matroid(kerA)
    # The list of circuits for ker(A).  This should be the minimal supports of the column space.
    CM=sorted([sorted(C) for C in M.circuits()])
    #print CM

#     for i in range(len(CM)):
#         H=deepcopy(G)
#         H.add_vertex(7)
#         for j in range(len(CM[i])):
#             H.add_edges([(7,CM[i][j])])
        #H.show()
        #print H.graph6_string(), ' with neighbors of 7 ', CM[i]
       
    #Construct all unions of supports in CM
    N=[i for i in range(len(CM))]
    S=[list(s) for s in subsets(N)]
    #print 'number of unions of column supports = ', len(S)

    # m=3500
    # print S[m], '\n'
    # U=[CM[k] for k in S[m]]
    # print list(set(flatten(U)))

    L=[]


    for j in range(len(S)):
         for k in range(len(S[j])):
            U=[CM[k] for k in S[j]]
            fU=list( set( flatten(U)))
            H=deepcopy(G)
            H.add_vertex(7)
            for i in range(len(fU)):
                H.add_edges([(7,fU[i])])
            #H.show()
            #print H.graph6_string()
            L.append(H.graph6_string())
    #Gets rid of duplicates in L
    L_new = list(set(L))

    m=len(L_new)
    L_new_remove=[]
    for i in range(m):
        for j in range(i+1,m):
            if Graph(L_new[i]).is_isomorphic(Graph(L_new[j])):
                L_new_remove.append(L_new[j])
    #print 'number of unique unions = ', len(L_new)
    L_new_new = list( set(L_new).difference( set(L_new_remove)) )
    #print 'number of non-isomorphic lifting graphs = ', len( L_new_new )
    #print list( L_new_new )
   
    return L_new_new;

counter = 0
determined = 0
for g in graphs(7):
    if g.vertex_connectivity()>=3:
        if find_Z(g)==4:
            is_min_rank_three = False
            counter += 1
            is_optimal_edge_set = False
            for edge in g.edges():
                if not is_optimal_edge_set:
                    g3 = g.copy()
                    g3.delete_edge(edge)
                    canon_label = g3.canonical_label().graph6_string()
                    if min_rank_dict.get(canon_label) == 2:
                        is_min_rank_three = True
                        is_optimal_edge_set = True
                        #print(canon_label)
                        #print(edge)
                        #print('The Graph has minimum rank 3')
                        g.show()
                        g3.show()
                        determined += 1
            for edge in g.complement().edges():
                 if not is_optimal_edge_set:
                    g3 = g.copy()
                    g3.add_edge(edge)
                    canon_label = g3.canonical_label().graph6_string()
                    if min_rank_dict.get(canon_label) == 2:
                        is_min_rank_three = True
                        is_optimal_edge_set = True
                        print(edge)
                        print(canon_label)
                        print('The Graph has minimum rank 3')
                        g.show()
                        g3.show()
                        determined += 1
            set_of_three = Combinations(g.vertices(),3)
            for bunch in set_of_three:
                if not is_min_rank_three:
                    h=g.subgraph(bunch)
                    if len(h.edges())==3: 
                        g1 = g.copy()
                        for edge in h.edges():
                            g1.delete_edge(edge)
                        possible_edges = Combinations(bunch,2)
                        edge_combinations = Combinations(possible_edges)
                        is_optimal_edge_set = False
                        for edge_set in edge_combinations:
                            if not is_optimal_edge_set:
                                g2 = g1.copy()
                                for edge in edge_set:
                                    g2.add_edge(edge)
                                canon_label = g2.canonical_label().graph6_string()
                                if min_rank_dict.get(canon_label) == 2:
                                    is_min_rank_three = True
                                    is_optimal_edge_set = True
                                    print(canon_label)
                                    print(bunch)
                                    print('The Graph has minimum rank 3')
                                    g.show()
                                    g2.show()
                                    determined += 1
                    elif len(h.edges())==2:
                        g1=g.copy()
                        for edge in h.edges():
                            g1.delete_edge(edge)
                        for edge in h.complement().edges():
                            g1.add_edge(edge)
                        edge_combinations = Combinations(h.edges())
                        is_optimal_edge_set = False
                        for edge_set in edge_combinations:
                            if not is_optimal_edge_set:
                                g2 = g1.copy()
                                for edge in edge_set:
                                    g2.add_edge(edge)
                                canon_label = g2.canonical_label().graph6_string()
                                if min_rank_dict.get(canon_label) == 2:
                                    is_min_rank_three = True
                                    is_optimal_edge_set = True
                                    print(canon_label)
                                    print(bunch)
                                    print('The Graph has minimum rank 3')
                                    g.show()
                                    g2.show()
                                    determined += 1
                    elif len(h.edges())==1:
                        g1=g.copy()
                        for edge in h.edges():
                            g1.delete_edge(edge)
                        for edge in h.complement().edges():
                            g1.add_edge(edge)
                        edge_combinations = Combinations(h.edges())
                        is_optimal_edge_set = False
                        for edge_set in edge_combinations:
                            if not is_optimal_edge_set:
                                g2 = g1.copy()
                                for edge in edge_set:
                                    g2.add_edge(edge)
                                canon_label = g2.canonical_label().graph6_string()
                                if min_rank_dict.get(canon_label) == 2:
                                    is_min_rank_three = True
                                    is_optimal_edge_set = True
                                    print(canon_label)
                                    print(bunch)
                                    print('The Graph has minimum rank 3')
                                    g.show()
                                    g2.show()  
                                    determined += 1
                    elif len(h.edges())==0:
                        g1=g.copy()
                        for edge in h.complement().edges():
                            g1.add_edge(edge)
                        canon_label = g1.canonical_label().graph6_string()
                        if min_rank_dict.get(canon_label) == 2:
                            is_min_rank_three = True
                            print(canon_label)
                            print(bunch)
                            print('The Graph has minimum rank 3')
                            g.show()
                            g2.show()   
                            determined += 1
            #if not is_min_rank_three:
                #g.show()

print(counter)
print(determined)


# Minimal Forts Function
# Author: Derek Hanely
# Last Updated: March 17, 2024
def minForts(G):
    """
    A brute-force algorithm for producing all minimal forts of a graph.

    INPUT: A simple, undirected graph G.

    OUTPUT: Returns a list of the minimal forts of G.
    """
    V=G.vertices(sort=True)
    forts=[]
    for F in powerset(V): # check if F is a fort of G
        if len(F)<=1: continue
        for u in Set(V).difference(Set(F)):
            neighbors = G.neighbors(u)
            if len(Set(F).intersection(Set(neighbors)))==1: break
        else:
            forts.append(F)
    uni_forts=[]
    for x in forts:
        if x not in uni_forts:
            uni_forts.append(x)

    min_forts=deepcopy(uni_forts)
    for x in uni_forts: # minimality check
        if any((Set(x).issuperset(Set(y)) and y!=x) for y in uni_forts):
            min_forts.remove(x)

    return min_forts
