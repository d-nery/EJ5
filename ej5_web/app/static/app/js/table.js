$(document).ready(() => {
  $('#tabela').DataTable({
      "ajax": 'http://127.0.0.1:5000/tabela',
      "columns": [
        { "data": "COD_BEM" },
        { "data": "UF" },
        { "data": "NUM_DOCFIS" },
        { "data": "COD_CFO_aquis" },
        { "data": "COD_CFO_rastr" },
        { "data": "COD_ESTAB_aquis" },
        { "data": "COD_ESTAB_rastr" },
        { "data": "COD_PRODUTO_aquis" },
        { "data": "COD_PRODUTO_rastr" },
        { "data": "DAT_OPER_aquis" },
        { "data": "DAT_OPER_rastr" },
        { "data": "VLR_CRED_DIF_ALIQ_aquis" },
        { "data": "VLR_CRED_DIF_ALIQ_rastr" },
        { "data": "VLR_CRED_ICMS_aquis" },
        { "data": "VLR_CRED_ICMS_rastr" },
        { "data": "VLR_ICMSS_aquis" },
        { "data": "VLR_ICMSS_rastr" },
    ]
  });
});
