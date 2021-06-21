
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftUNOTleftMAYORIGUALMAYORQUEMENORIGUALMENORQUEDIFERENTEIGUALIGUALleftMASMENOSleftMODPORDIVnonassocPOTrightUMENOSrightUMASMASrightUMENOSMENOSAND CADENA CHAR COMA CORA CORC DECIMAL DIFERENTE DIV DOSPUNTOS ENTERO ID IGUAL IGUALIGUAL LLAVEA LLAVEC MAS MASMAS MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MENOS MENOSMENOS MOD NOT NULO OR PARA PARC POR POT PUNTOCOMA RBOOLEAN RBREAK RCASE RCONTINUE RDEFAULT RELSE RFALSE RFLOAT RFOR RFUNC RIF RINT RMAIN RNULL RPRINT RSTRING RSWITCH RTRUE RVAR RWHILEinit               : instruccionesinstrucciones      : instrucciones instruccioninstrucciones      : instruccionterminacion        : PUNTOCOMA\n                          |\n    instruccion      : imprimir_instr terminacion\n                        | declaracion_instr terminacion\n                        | asignacion_instr terminacion\n                        | if_instr\n                        | switch_instr\n                        | while_instr\n                        | for_instr\n                        | break_instr terminacion\n                        | continue_instr terminacion\n                        | main_instr\n                        | funcion_instr\n                        | llamada_instr terminacion\n                        | incremento_instr terminacion\n                        | decremento_instr terminacion\n                        imprimir_instr     : RPRINT PARA expresion PARCdeclaracion_instr     : RVAR ID IGUAL expresiondeclaracion_instr     : RVAR IDasignacion_instr     : ID IGUAL expresionincremento_instr     : ID MASMASdecremento_instr     : ID MENOSMENOSif_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVECif_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVECif_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instrswitch_instr     : RSWITCH PARA expresion PARC LLAVEA cases_list default LLAVECswitch_instr     : RSWITCH PARA expresion PARC LLAVEA cases_list LLAVECswitch_instr     : RSWITCH PARA expresion PARC LLAVEA default LLAVECcases_list       : cases_list casecases_list       : casecase             : RCASE expresion DOSPUNTOS instruccionesdefault          : RDEFAULT DOSPUNTOS instruccioneswhile_instr     : RWHILE PARA expresion PARC LLAVEA instrucciones LLAVECfor_instr     : RFOR PARA declaracion_asignacion PUNTOCOMA expresion PUNTOCOMA actualizacion PARC LLAVEA instrucciones LLAVECdeclaracion_asignacion   :   declaracion_instr\n                                |   asignacion_instractualizacion    :   incremento_instr\n                        |   decremento_instr\n                        |   asignacion_instr\n                        break_instr     : RBREAKcontinue_instr     : RCONTINUEmain_instr     : RMAIN PARA PARC LLAVEA instrucciones LLAVECfuncion_instr     : RFUNC ID PARA PARC LLAVEA instrucciones LLAVECllamada_instr     : ID PARA PARC\n    expresion           : expresion MAS expresion\n                        | expresion MENOS expresion\n                        | expresion POR expresion\n                        | expresion DIV expresion\n                        | expresion MOD expresion\n                        | expresion POT expresion\n                        | expresion MENORQUE expresion\n                        | expresion MAYORQUE expresion\n                        | expresion MENORIGUAL expresion\n                        | expresion MAYORIGUAL expresion\n                        | expresion IGUALIGUAL expresion\n                        | expresion DIFERENTE expresion\n                        | expresion AND expresion\n                        | expresion OR expresion\n    \n    expresion           : MENOS expresion %prec UMENOS\n                        | NOT expresion %prec UNOT\n                        | expresion MENOSMENOS %prec UMENOSMENOS\n                        | expresion MASMAS %prec UMASMAS\n    \n    expresion           : PARA expresion PARC\n    expresion        : IDexpresion        : ENTEROexpresion        : DECIMALexpresion        : CADENAexpresion        : CHARexpresion        : RNULLexpresion : RTRUEexpresion : RFALSEinstruccion        : error PUNTOCOMAinstruccion        : error'
    
_lr_action_items = {'error':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,26,27,30,31,32,33,34,35,36,37,38,39,40,42,45,46,57,58,59,60,61,62,63,64,66,67,78,93,94,95,96,97,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,123,124,125,131,133,134,135,137,139,140,142,148,150,151,152,154,155,156,157,158,159,160,161,],[18,18,-3,-5,-5,-5,-9,-10,-11,-12,-5,-5,-15,-16,-5,-5,-5,-76,-43,-44,-2,-6,-4,-7,-8,-13,-14,-17,-18,-19,-75,-22,-24,-25,-67,-68,-69,-70,-71,-72,-73,-74,-23,-47,-20,-64,-65,-62,-63,-21,18,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,18,18,18,18,18,18,-45,18,-26,-30,-31,18,-36,-46,-29,18,18,18,-28,18,18,18,18,-27,-37,]),'RPRINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,26,27,30,31,32,33,34,35,36,37,38,39,40,42,45,46,57,58,59,60,61,62,63,64,66,67,78,93,94,95,96,97,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,123,124,125,131,133,134,135,137,139,140,142,148,150,151,152,154,155,156,157,158,159,160,161,],[19,19,-3,-5,-5,-5,-9,-10,-11,-12,-5,-5,-15,-16,-5,-5,-5,-76,-43,-44,-2,-6,-4,-7,-8,-13,-14,-17,-18,-19,-75,-22,-24,-25,-67,-68,-69,-70,-71,-72,-73,-74,-23,-47,-20,-64,-65,-62,-63,-21,19,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,19,19,19,19,19,19,-45,19,-26,-30,-31,19,-36,-46,-29,19,19,19,-28,19,19,19,19,-27,-37,]),'RVAR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,26,27,30,31,32,33,34,35,36,37,38,39,40,42,45,46,50,57,58,59,60,61,62,63,64,66,67,78,93,94,95,96,97,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,123,124,125,131,133,134,135,137,139,140,142,148,150,151,152,154,155,156,157,158,159,160,161,],[20,20,-3,-5,-5,-5,-9,-10,-11,-12,-5,-5,-15,-16,-5,-5,-5,-76,-43,-44,-2,-6,-4,-7,-8,-13,-14,-17,-18,-19,-75,-22,-24,-25,20,-67,-68,-69,-70,-71,-72,-73,-74,-23,-47,-20,-64,-65,-62,-63,-21,20,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,20,20,20,20,20,20,-45,20,-26,-30,-31,20,-36,-46,-29,20,20,20,-28,20,20,20,20,-27,-37,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,26,27,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,48,49,50,53,55,56,57,58,59,60,61,62,63,64,65,66,67,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,101,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,123,124,125,130,131,132,133,134,135,137,139,140,142,148,150,151,152,154,155,156,157,158,159,160,161,],[21,21,-3,-5,-5,-5,-9,-10,-11,-12,-5,-5,-15,-16,-5,-5,-5,-76,42,-43,-44,52,-2,-6,-4,-7,-8,-13,-14,-17,-18,-19,-75,57,-22,57,-24,-25,57,57,57,74,57,57,57,-67,-68,-69,-70,-71,-72,-73,-74,57,-23,-47,-20,57,57,57,57,57,57,57,57,57,57,57,57,57,57,-64,-65,-62,-63,-21,57,21,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,21,21,21,21,21,57,21,147,-45,21,-26,-30,-31,21,-36,-46,-29,21,21,21,-28,21,21,21,21,-27,-37,]),'RIF':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,26,27,30,31,32,33,34,35,36,37,38,39,40,42,45,46,57,58,59,60,61,62,63,64,66,67,78,93,94,95,96,97,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,123,124,125,131,133,134,135,137,139,140,142,148,149,150,151,152,154,155,156,157,158,159,160,161,],[22,22,-3,-5,-5,-5,-9,-10,-11,-12,-5,-5,-15,-16,-5,-5,-5,-76,-43,-44,-2,-6,-4,-7,-8,-13,-14,-17,-18,-19,-75,-22,-24,-25,-67,-68,-69,-70,-71,-72,-73,-74,-23,-47,-20,-64,-65,-62,-63,-21,22,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,22,22,22,22,22,22,-45,22,-26,-30,-31,22,-36,-46,22,-29,22,22,22,-28,22,22,22,22,-27,-37,]),'RSWITCH':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,26,27,30,31,32,33,34,35,36,37,38,39,40,42,45,46,57,58,59,60,61,62,63,64,66,67,78,93,94,95,96,97,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,123,124,125,131,133,134,135,137,139,140,142,148,150,151,152,154,155,156,157,158,159,160,161,],[23,23,-3,-5,-5,-5,-9,-10,-11,-12,-5,-5,-15,-16,-5,-5,-5,-76,-43,-44,-2,-6,-4,-7,-8,-13,-14,-17,-18,-19,-75,-22,-24,-25,-67,-68,-69,-70,-71,-72,-73,-74,-23,-47,-20,-64,-65,-62,-63,-21,23,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,23,23,23,23,23,23,-45,23,-26,-30,-31,23,-36,-46,-29,23,23,23,-28,23,23,23,23,-27,-37,]),'RWHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,26,27,30,31,32,33,34,35,36,37,38,39,40,42,45,46,57,58,59,60,61,62,63,64,66,67,78,93,94,95,96,97,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,123,124,125,131,133,134,135,137,139,140,142,148,150,151,152,154,155,156,157,158,159,160,161,],[24,24,-3,-5,-5,-5,-9,-10,-11,-12,-5,-5,-15,-16,-5,-5,-5,-76,-43,-44,-2,-6,-4,-7,-8,-13,-14,-17,-18,-19,-75,-22,-24,-25,-67,-68,-69,-70,-71,-72,-73,-74,-23,-47,-20,-64,-65,-62,-63,-21,24,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,24,24,24,24,24,24,-45,24,-26,-30,-31,24,-36,-46,-29,24,24,24,-28,24,24,24,24,-27,-37,]),'RFOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,26,27,30,31,32,33,34,35,36,37,38,39,40,42,45,46,57,58,59,60,61,62,63,64,66,67,78,93,94,95,96,97,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,123,124,125,131,133,134,135,137,139,140,142,148,150,151,152,154,155,156,157,158,159,160,161,],[25,25,-3,-5,-5,-5,-9,-10,-11,-12,-5,-5,-15,-16,-5,-5,-5,-76,-43,-44,-2,-6,-4,-7,-8,-13,-14,-17,-18,-19,-75,-22,-24,-25,-67,-68,-69,-70,-71,-72,-73,-74,-23,-47,-20,-64,-65,-62,-63,-21,25,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,25,25,25,25,25,25,-45,25,-26,-30,-31,25,-36,-46,-29,25,25,25,-28,25,25,25,25,-27,-37,]),'RBREAK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,26,27,30,31,32,33,34,35,36,37,38,39,40,42,45,46,57,58,59,60,61,62,63,64,66,67,78,93,94,95,96,97,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,123,124,125,131,133,134,135,137,139,140,142,148,150,151,152,154,155,156,157,158,159,160,161,],[26,26,-3,-5,-5,-5,-9,-10,-11,-12,-5,-5,-15,-16,-5,-5,-5,-76,-43,-44,-2,-6,-4,-7,-8,-13,-14,-17,-18,-19,-75,-22,-24,-25,-67,-68,-69,-70,-71,-72,-73,-74,-23,-47,-20,-64,-65,-62,-63,-21,26,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,26,26,26,26,26,26,-45,26,-26,-30,-31,26,-36,-46,-29,26,26,26,-28,26,26,26,26,-27,-37,]),'RCONTINUE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,26,27,30,31,32,33,34,35,36,37,38,39,40,42,45,46,57,58,59,60,61,62,63,64,66,67,78,93,94,95,96,97,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,123,124,125,131,133,134,135,137,139,140,142,148,150,151,152,154,155,156,157,158,159,160,161,],[27,27,-3,-5,-5,-5,-9,-10,-11,-12,-5,-5,-15,-16,-5,-5,-5,-76,-43,-44,-2,-6,-4,-7,-8,-13,-14,-17,-18,-19,-75,-22,-24,-25,-67,-68,-69,-70,-71,-72,-73,-74,-23,-47,-20,-64,-65,-62,-63,-21,27,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,27,27,27,27,27,27,-45,27,-26,-30,-31,27,-36,-46,-29,27,27,27,-28,27,27,27,27,-27,-37,]),'RMAIN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,26,27,30,31,32,33,34,35,36,37,38,39,40,42,45,46,57,58,59,60,61,62,63,64,66,67,78,93,94,95,96,97,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,123,124,125,131,133,134,135,137,139,140,142,148,150,151,152,154,155,156,157,158,159,160,161,],[28,28,-3,-5,-5,-5,-9,-10,-11,-12,-5,-5,-15,-16,-5,-5,-5,-76,-43,-44,-2,-6,-4,-7,-8,-13,-14,-17,-18,-19,-75,-22,-24,-25,-67,-68,-69,-70,-71,-72,-73,-74,-23,-47,-20,-64,-65,-62,-63,-21,28,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,28,28,28,28,28,28,-45,28,-26,-30,-31,28,-36,-46,-29,28,28,28,-28,28,28,28,28,-27,-37,]),'RFUNC':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,26,27,30,31,32,33,34,35,36,37,38,39,40,42,45,46,57,58,59,60,61,62,63,64,66,67,78,93,94,95,96,97,102,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,123,124,125,131,133,134,135,137,139,140,142,148,150,151,152,154,155,156,157,158,159,160,161,],[29,29,-3,-5,-5,-5,-9,-10,-11,-12,-5,-5,-15,-16,-5,-5,-5,-76,-43,-44,-2,-6,-4,-7,-8,-13,-14,-17,-18,-19,-75,-22,-24,-25,-67,-68,-69,-70,-71,-72,-73,-74,-23,-47,-20,-64,-65,-62,-63,-21,29,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,29,29,29,29,29,29,-45,29,-26,-30,-31,29,-36,-46,-29,29,29,29,-28,29,29,29,29,-27,-37,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,26,27,30,31,32,33,34,35,36,37,38,39,40,42,45,46,57,58,59,60,61,62,63,64,66,67,78,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,133,135,137,139,142,148,150,155,160,161,],[0,-1,-3,-5,-5,-5,-9,-10,-11,-12,-5,-5,-15,-16,-5,-5,-5,-76,-43,-44,-2,-6,-4,-7,-8,-13,-14,-17,-18,-19,-75,-22,-24,-25,-67,-68,-69,-70,-71,-72,-73,-74,-23,-47,-20,-64,-65,-62,-63,-21,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,-45,-26,-30,-31,-36,-46,-29,-28,-27,-37,]),'LLAVEC':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,26,27,30,31,32,33,34,35,36,37,38,39,40,42,45,46,57,58,59,60,61,62,63,64,66,67,78,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,123,125,126,127,128,131,133,134,135,136,137,138,139,142,148,150,151,155,156,158,159,160,161,],[-3,-5,-5,-5,-9,-10,-11,-12,-5,-5,-15,-16,-5,-5,-5,-76,-43,-44,-2,-6,-4,-7,-8,-13,-14,-17,-18,-19,-75,-22,-24,-25,-67,-68,-69,-70,-71,-72,-73,-74,-23,-47,-20,-64,-65,-62,-63,-21,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,133,135,137,139,-33,142,-45,148,-26,150,-30,-32,-31,-36,-46,-29,-35,-28,-34,160,161,-27,-37,]),'RDEFAULT':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,26,27,30,31,32,33,34,35,36,37,38,39,40,42,45,46,57,58,59,60,61,62,63,64,66,67,78,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,126,128,133,135,137,138,139,142,148,150,155,156,160,161,],[-3,-5,-5,-5,-9,-10,-11,-12,-5,-5,-15,-16,-5,-5,-5,-76,-43,-44,-2,-6,-4,-7,-8,-13,-14,-17,-18,-19,-75,-22,-24,-25,-67,-68,-69,-70,-71,-72,-73,-74,-23,-47,-20,-64,-65,-62,-63,-21,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,129,129,-33,-45,-26,-30,-32,-31,-36,-46,-29,-28,-34,-27,-37,]),'RCASE':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,26,27,30,31,32,33,34,35,36,37,38,39,40,42,45,46,57,58,59,60,61,62,63,64,66,67,78,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,120,126,128,133,135,137,138,139,142,148,150,155,156,160,161,],[-3,-5,-5,-5,-9,-10,-11,-12,-5,-5,-15,-16,-5,-5,-5,-76,-43,-44,-2,-6,-4,-7,-8,-13,-14,-17,-18,-19,-75,-22,-24,-25,-67,-68,-69,-70,-71,-72,-73,-74,-23,-47,-20,-64,-65,-62,-63,-21,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,130,130,-33,-45,-26,-30,-32,-31,-36,-46,-29,-28,-34,-27,-37,]),'PUNTOCOMA':([4,5,6,11,12,15,16,17,18,26,27,42,45,46,57,58,59,60,61,62,63,64,66,67,71,72,73,78,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,],[32,32,32,32,32,32,32,32,40,-43,-44,-22,-24,-25,-67,-68,-69,-70,-71,-72,-73,-74,-23,-47,101,-38,-39,-20,-64,-65,-62,-63,-21,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,132,]),'PARA':([19,21,22,23,24,25,28,41,43,47,48,49,52,53,55,56,65,79,80,81,82,83,84,85,86,87,88,89,90,91,92,101,130,],[41,44,47,48,49,50,51,53,53,53,53,53,76,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'IGUAL':([21,42,74,147,],[43,65,43,43,]),'MASMAS':([21,54,57,58,59,60,61,62,63,64,66,68,69,70,77,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,141,147,],[45,94,-67,-68,-69,-70,-71,-72,-73,-74,94,94,94,94,94,-64,-65,-62,-63,94,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,94,94,45,]),'MENOSMENOS':([21,54,57,58,59,60,61,62,63,64,66,68,69,70,77,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,141,147,],[46,93,-67,-68,-69,-70,-71,-72,-73,-74,93,93,93,93,93,-64,-65,-62,-63,93,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,93,93,46,]),'MENOS':([41,43,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,101,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,130,141,],[55,55,55,55,55,55,80,55,55,-67,-68,-69,-70,-71,-72,-73,-74,55,80,80,80,80,80,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-64,-65,-62,80,80,55,-66,-48,-49,-50,-51,-52,-53,80,80,80,80,80,80,80,80,80,55,80,]),'NOT':([41,43,47,48,49,53,55,56,65,79,80,81,82,83,84,85,86,87,88,89,90,91,92,101,130,],[56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'ENTERO':([41,43,47,48,49,53,55,56,65,79,80,81,82,83,84,85,86,87,88,89,90,91,92,101,130,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'DECIMAL':([41,43,47,48,49,53,55,56,65,79,80,81,82,83,84,85,86,87,88,89,90,91,92,101,130,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'CADENA':([41,43,47,48,49,53,55,56,65,79,80,81,82,83,84,85,86,87,88,89,90,91,92,101,130,],[60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'CHAR':([41,43,47,48,49,53,55,56,65,79,80,81,82,83,84,85,86,87,88,89,90,91,92,101,130,],[61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,]),'RNULL':([41,43,47,48,49,53,55,56,65,79,80,81,82,83,84,85,86,87,88,89,90,91,92,101,130,],[62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,]),'RTRUE':([41,43,47,48,49,53,55,56,65,79,80,81,82,83,84,85,86,87,88,89,90,91,92,101,130,],[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,]),'RFALSE':([41,43,47,48,49,53,55,56,65,79,80,81,82,83,84,85,86,87,88,89,90,91,92,101,130,],[64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'PARC':([44,45,46,51,54,57,58,59,60,61,62,63,64,66,68,69,70,76,77,93,94,95,96,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,143,144,145,146,],[67,-24,-25,75,78,-67,-68,-69,-70,-71,-72,-73,-74,-23,98,99,100,103,104,-64,-65,-62,-63,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,153,-40,-41,-42,]),'MAS':([54,57,58,59,60,61,62,63,64,66,68,69,70,77,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,141,],[79,-67,-68,-69,-70,-71,-72,-73,-74,79,79,79,79,79,-64,-65,-62,79,79,-66,-48,-49,-50,-51,-52,-53,79,79,79,79,79,79,79,79,79,79,]),'POR':([54,57,58,59,60,61,62,63,64,66,68,69,70,77,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,141,],[81,-67,-68,-69,-70,-71,-72,-73,-74,81,81,81,81,81,-64,-65,-62,81,81,-66,81,81,-50,-51,-52,-53,81,81,81,81,81,81,81,81,81,81,]),'DIV':([54,57,58,59,60,61,62,63,64,66,68,69,70,77,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,141,],[82,-67,-68,-69,-70,-71,-72,-73,-74,82,82,82,82,82,-64,-65,-62,82,82,-66,82,82,-50,-51,-52,-53,82,82,82,82,82,82,82,82,82,82,]),'MOD':([54,57,58,59,60,61,62,63,64,66,68,69,70,77,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,141,],[83,-67,-68,-69,-70,-71,-72,-73,-74,83,83,83,83,83,-64,-65,-62,83,83,-66,83,83,-50,-51,-52,-53,83,83,83,83,83,83,83,83,83,83,]),'POT':([54,57,58,59,60,61,62,63,64,66,68,69,70,77,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,141,],[84,-67,-68,-69,-70,-71,-72,-73,-74,84,84,84,84,84,-64,-65,-62,84,84,-66,84,84,84,84,84,None,84,84,84,84,84,84,84,84,84,84,]),'MENORQUE':([54,57,58,59,60,61,62,63,64,66,68,69,70,77,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,141,],[85,-67,-68,-69,-70,-71,-72,-73,-74,85,85,85,85,85,-64,-65,-62,85,85,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,85,85,85,85,]),'MAYORQUE':([54,57,58,59,60,61,62,63,64,66,68,69,70,77,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,141,],[86,-67,-68,-69,-70,-71,-72,-73,-74,86,86,86,86,86,-64,-65,-62,86,86,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,86,86,86,86,]),'MENORIGUAL':([54,57,58,59,60,61,62,63,64,66,68,69,70,77,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,141,],[87,-67,-68,-69,-70,-71,-72,-73,-74,87,87,87,87,87,-64,-65,-62,87,87,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,87,87,87,87,]),'MAYORIGUAL':([54,57,58,59,60,61,62,63,64,66,68,69,70,77,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,141,],[88,-67,-68,-69,-70,-71,-72,-73,-74,88,88,88,88,88,-64,-65,-62,88,88,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,88,88,88,88,]),'IGUALIGUAL':([54,57,58,59,60,61,62,63,64,66,68,69,70,77,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,141,],[89,-67,-68,-69,-70,-71,-72,-73,-74,89,89,89,89,89,-64,-65,-62,89,89,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,89,89,89,89,]),'DIFERENTE':([54,57,58,59,60,61,62,63,64,66,68,69,70,77,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,141,],[90,-67,-68,-69,-70,-71,-72,-73,-74,90,90,90,90,90,-64,-65,-62,90,90,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,90,90,90,90,]),'AND':([54,57,58,59,60,61,62,63,64,66,68,69,70,77,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,141,],[91,-67,-68,-69,-70,-71,-72,-73,-74,91,91,91,91,91,-64,-65,-62,-63,91,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,91,91,91,]),'OR':([54,57,58,59,60,61,62,63,64,66,68,69,70,77,93,94,95,96,97,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,141,],[92,-67,-68,-69,-70,-71,-72,-73,-74,92,92,92,92,92,-64,-65,-62,-63,92,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,92,92,]),'DOSPUNTOS':([57,58,59,60,61,62,63,64,93,94,95,96,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,129,141,],[-67,-68,-69,-70,-71,-72,-73,-74,-64,-65,-62,-63,-66,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-58,-59,-60,-61,140,152,]),'LLAVEA':([75,98,99,100,103,149,153,],[102,119,120,121,124,154,157,]),'RELSE':([135,],[149,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'instrucciones':([0,102,119,121,124,140,152,154,157,],[2,123,125,131,134,151,156,158,159,]),'instruccion':([0,2,102,119,121,123,124,125,131,134,140,151,152,154,156,157,158,159,],[3,30,3,3,3,30,3,30,30,30,3,30,3,3,30,3,30,30,]),'imprimir_instr':([0,2,102,119,121,123,124,125,131,134,140,151,152,154,156,157,158,159,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'declaracion_instr':([0,2,50,102,119,121,123,124,125,131,134,140,151,152,154,156,157,158,159,],[5,5,72,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'asignacion_instr':([0,2,50,102,119,121,123,124,125,131,132,134,140,151,152,154,156,157,158,159,],[6,6,73,6,6,6,6,6,6,6,146,6,6,6,6,6,6,6,6,6,]),'if_instr':([0,2,102,119,121,123,124,125,131,134,140,149,151,152,154,156,157,158,159,],[7,7,7,7,7,7,7,7,7,7,7,155,7,7,7,7,7,7,7,]),'switch_instr':([0,2,102,119,121,123,124,125,131,134,140,151,152,154,156,157,158,159,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'while_instr':([0,2,102,119,121,123,124,125,131,134,140,151,152,154,156,157,158,159,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'for_instr':([0,2,102,119,121,123,124,125,131,134,140,151,152,154,156,157,158,159,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'break_instr':([0,2,102,119,121,123,124,125,131,134,140,151,152,154,156,157,158,159,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'continue_instr':([0,2,102,119,121,123,124,125,131,134,140,151,152,154,156,157,158,159,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'main_instr':([0,2,102,119,121,123,124,125,131,134,140,151,152,154,156,157,158,159,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'funcion_instr':([0,2,102,119,121,123,124,125,131,134,140,151,152,154,156,157,158,159,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'llamada_instr':([0,2,102,119,121,123,124,125,131,134,140,151,152,154,156,157,158,159,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'incremento_instr':([0,2,102,119,121,123,124,125,131,132,134,140,151,152,154,156,157,158,159,],[16,16,16,16,16,16,16,16,16,144,16,16,16,16,16,16,16,16,16,]),'decremento_instr':([0,2,102,119,121,123,124,125,131,132,134,140,151,152,154,156,157,158,159,],[17,17,17,17,17,17,17,17,17,145,17,17,17,17,17,17,17,17,17,]),'terminacion':([4,5,6,11,12,15,16,17,],[31,33,34,35,36,37,38,39,]),'expresion':([41,43,47,48,49,53,55,56,65,79,80,81,82,83,84,85,86,87,88,89,90,91,92,101,130,],[54,66,68,69,70,77,95,96,97,105,106,107,108,109,110,111,112,113,114,115,116,117,118,122,141,]),'declaracion_asignacion':([50,],[71,]),'cases_list':([120,],[126,]),'default':([120,126,],[127,136,]),'case':([120,126,],[128,138,]),'actualizacion':([132,],[143,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> instrucciones','init',1,'p_init','grammar.py',242),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instrucciones_instruccion','grammar.py',246),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','grammar.py',254),
  ('terminacion -> PUNTOCOMA','terminacion',1,'p_terminacion','grammar.py',262),
  ('terminacion -> <empty>','terminacion',0,'p_terminacion','grammar.py',263),
  ('instruccion -> imprimir_instr terminacion','instruccion',2,'p_instruccion','grammar.py',269),
  ('instruccion -> declaracion_instr terminacion','instruccion',2,'p_instruccion','grammar.py',270),
  ('instruccion -> asignacion_instr terminacion','instruccion',2,'p_instruccion','grammar.py',271),
  ('instruccion -> if_instr','instruccion',1,'p_instruccion','grammar.py',272),
  ('instruccion -> switch_instr','instruccion',1,'p_instruccion','grammar.py',273),
  ('instruccion -> while_instr','instruccion',1,'p_instruccion','grammar.py',274),
  ('instruccion -> for_instr','instruccion',1,'p_instruccion','grammar.py',275),
  ('instruccion -> break_instr terminacion','instruccion',2,'p_instruccion','grammar.py',276),
  ('instruccion -> continue_instr terminacion','instruccion',2,'p_instruccion','grammar.py',277),
  ('instruccion -> main_instr','instruccion',1,'p_instruccion','grammar.py',278),
  ('instruccion -> funcion_instr','instruccion',1,'p_instruccion','grammar.py',279),
  ('instruccion -> llamada_instr terminacion','instruccion',2,'p_instruccion','grammar.py',280),
  ('instruccion -> incremento_instr terminacion','instruccion',2,'p_instruccion','grammar.py',281),
  ('instruccion -> decremento_instr terminacion','instruccion',2,'p_instruccion','grammar.py',282),
  ('imprimir_instr -> RPRINT PARA expresion PARC','imprimir_instr',4,'p_imprimir','grammar.py',294),
  ('declaracion_instr -> RVAR ID IGUAL expresion','declaracion_instr',4,'p_declaracion','grammar.py',299),
  ('declaracion_instr -> RVAR ID','declaracion_instr',2,'p_declaracion_1','grammar.py',303),
  ('asignacion_instr -> ID IGUAL expresion','asignacion_instr',3,'p_asignacion','grammar.py',310),
  ('incremento_instr -> ID MASMAS','incremento_instr',2,'p_incremento','grammar.py',316),
  ('decremento_instr -> ID MENOSMENOS','decremento_instr',2,'p_decremento','grammar.py',322),
  ('if_instr -> RIF PARA expresion PARC LLAVEA instrucciones LLAVEC','if_instr',7,'p_if_1','grammar.py',329),
  ('if_instr -> RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVEC','if_instr',11,'p_if_2','grammar.py',333),
  ('if_instr -> RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instr','if_instr',9,'p_if_3','grammar.py',337),
  ('switch_instr -> RSWITCH PARA expresion PARC LLAVEA cases_list default LLAVEC','switch_instr',8,'p_switch_1','grammar.py',343),
  ('switch_instr -> RSWITCH PARA expresion PARC LLAVEA cases_list LLAVEC','switch_instr',7,'p_switch_2','grammar.py',347),
  ('switch_instr -> RSWITCH PARA expresion PARC LLAVEA default LLAVEC','switch_instr',7,'p_switch_3','grammar.py',351),
  ('cases_list -> cases_list case','cases_list',2,'p_cases_list_cases_list_case','grammar.py',355),
  ('cases_list -> case','cases_list',1,'p_cases_list_case','grammar.py',361),
  ('case -> RCASE expresion DOSPUNTOS instrucciones','case',4,'p_case','grammar.py',368),
  ('default -> RDEFAULT DOSPUNTOS instrucciones','default',3,'p_default','grammar.py',372),
  ('while_instr -> RWHILE PARA expresion PARC LLAVEA instrucciones LLAVEC','while_instr',7,'p_while','grammar.py',378),
  ('for_instr -> RFOR PARA declaracion_asignacion PUNTOCOMA expresion PUNTOCOMA actualizacion PARC LLAVEA instrucciones LLAVEC','for_instr',11,'p_for','grammar.py',384),
  ('declaracion_asignacion -> declaracion_instr','declaracion_asignacion',1,'p_declaracion_asignacion','grammar.py',393),
  ('declaracion_asignacion -> asignacion_instr','declaracion_asignacion',1,'p_declaracion_asignacion','grammar.py',394),
  ('actualizacion -> incremento_instr','actualizacion',1,'p_actualizacion','grammar.py',400),
  ('actualizacion -> decremento_instr','actualizacion',1,'p_actualizacion','grammar.py',401),
  ('actualizacion -> asignacion_instr','actualizacion',1,'p_actualizacion','grammar.py',402),
  ('break_instr -> RBREAK','break_instr',1,'p_break','grammar.py',409),
  ('continue_instr -> RCONTINUE','continue_instr',1,'p_continue','grammar.py',415),
  ('main_instr -> RMAIN PARA PARC LLAVEA instrucciones LLAVEC','main_instr',6,'p_main','grammar.py',421),
  ('funcion_instr -> RFUNC ID PARA PARC LLAVEA instrucciones LLAVEC','funcion_instr',7,'p_funcion','grammar.py',428),
  ('llamada_instr -> ID PARA PARC','llamada_instr',3,'p_llamada','grammar.py',434),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','grammar.py',458),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','grammar.py',459),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','grammar.py',460),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_binaria','grammar.py',461),
  ('expresion -> expresion MOD expresion','expresion',3,'p_expresion_binaria','grammar.py',462),
  ('expresion -> expresion POT expresion','expresion',3,'p_expresion_binaria','grammar.py',463),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_expresion_binaria','grammar.py',464),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_expresion_binaria','grammar.py',465),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_binaria','grammar.py',466),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_binaria','grammar.py',467),
  ('expresion -> expresion IGUALIGUAL expresion','expresion',3,'p_expresion_binaria','grammar.py',468),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_binaria','grammar.py',469),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_binaria','grammar.py',470),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_binaria','grammar.py',471),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','grammar.py',505),
  ('expresion -> NOT expresion','expresion',2,'p_expresion_unaria','grammar.py',506),
  ('expresion -> expresion MENOSMENOS','expresion',2,'p_expresion_unaria','grammar.py',507),
  ('expresion -> expresion MASMAS','expresion',2,'p_expresion_unaria','grammar.py',508),
  ('expresion -> PARA expresion PARC','expresion',3,'p_expresion_agrupacion','grammar.py',522),
  ('expresion -> ID','expresion',1,'p_expresion_identificador','grammar.py',527),
  ('expresion -> ENTERO','expresion',1,'p_expresion_entero','grammar.py',531),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','grammar.py',535),
  ('expresion -> CADENA','expresion',1,'p_expresion_cadena','grammar.py',539),
  ('expresion -> CHAR','expresion',1,'p_expresion_char','grammar.py',543),
  ('expresion -> RNULL','expresion',1,'p_expresion_null','grammar.py',547),
  ('expresion -> RTRUE','expresion',1,'p_expresion_true','grammar.py',551),
  ('expresion -> RFALSE','expresion',1,'p_expresion_false','grammar.py',555),
  ('instruccion -> error PUNTOCOMA','instruccion',2,'p_instruccion_error','grammar.py',567),
  ('instruccion -> error','instruccion',1,'p_instruccion_error1','grammar.py',572),
]
