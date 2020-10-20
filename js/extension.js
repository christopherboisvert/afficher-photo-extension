(function() {
  class VoirMaPhotoExtension extends window.Extension {
    constructor() {
      super('voir-ma-photo');
      this.addMenuEntry('Voir ma photo');

      this.content = '';
      fetch(`/extensions/${this.id}/views/content.html`)
        .then((res) => res.text())
        .then((text) => {
          this.content = text;
        })
        .catch((e) => console.error('Incapable d\'afficher le contenu :', e));
    }

    show() {
      this.view.innerHTML = this.content;

      const submit =
        document.getElementById('extension-voir-ma-photo-form-submit');
      const image =
        document.getElementById('extension-voir-ma-photo-photo');

      submit.addEventListener('click', () => {
        fetch(`/extensions/${this.id}/api/voir-ma-photo`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            Accept: 'application/json',
            Authorization: `Bearer ${window.API.jwt}`,
          },
          body: "",
        }).then((res) => {
          return res.json();
        }).then((body) => {
          if(body.afficher_photo == true)
          {
            image.visibility = true;
          }
        }).catch((e) => {
          pre.innerText = e.toString();
        });
      });
    }
  }

  new VoirMaPhotoExtension();
})();
