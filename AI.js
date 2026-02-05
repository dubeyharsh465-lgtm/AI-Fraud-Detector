 async function sendAudio() {
      const file = document.getElementById("audioFile").files[0];

      if (!file) {
        alert("Please upload an MP3 file!");
        return;
      }

      const reader = new FileReader();
      reader.readAsDataURL(file);

      reader.onload = async function () {
        const base64Audio = reader.result.split(",")[1];

        const response = await fetch("http://localhost:8000/api/voice-detection", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "x-api-key": "sk_test_123456789"
          },
          body: JSON.stringify({
            language: document.getElementById("language").value,
            audioFormat: "mp3",
            audioBase64: base64Audio
          })
        });
        
        const result = await response.json();

        document.getElementById("output").textContent =
          JSON.stringify(result, null, 2);
      };
    }