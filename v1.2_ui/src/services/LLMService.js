export default function callLLM(prompt) {
    const URL = "/api/ask"
    const body = { query: prompt }
    return fetch(URL, {
        method: "POST",
        body: JSON.stringify(body),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
    })
    .then((response) => response.json())
    .then(data => { return data.result.answer });
}