    function handleForm(e) {
      e.preventDefault(); //impede o formulário de tentar recarregar a página do jeito antigo
      const nome = document.getElementById('nomeInput').value.trim();
      if (nome) window.location.href = '/saudacao/' + encodeURIComponent(nome);
    }

    const filenames = {
      'tab-main': 'main.py',
      // 'tab-index': 'index.html',
      // 'tab-saudacao': 'saudacao.html',
      // 'tab-style': 'style.css' – n precisamos usar
    };

    function switchTab(e, id) {
      document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
      e.target.classList.add('active');
      document.getElementById(id).classList.add('active');
      document.getElementById('code-filename').textContent = filenames[id];
    }