

  function show_popup(e) {
    e.preventDefault();
    var v1 = document.getElementById('mname').value;
    var v2 = document.getElementById('gemail').value;
    var v3 = document.getElementById('suname').value;
    var v4 = document.getElementById('tlname').value;
    const wdw = window.open('', 'formpopup', 'width=400,height=400,resizeable,scrollbars');
    wdw.document.body.textContent = ' Manager Name:    ' + v1 + ' Group email :    ' + v2 + '  Server Name:    ' + v3 + ' Team lead  Name:     ' + v4;
}