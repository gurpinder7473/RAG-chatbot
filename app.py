import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="DocMind RAG Chatbot", layout="wide")
st.title("DocMind – Streamlit Wrapper")
st.caption("Your original HTML app is embedded below.")

html_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>DocMind – RAG Chatbot</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --accent: #1D9E75;
      --accent-dark: #0F6E56;
      --accent-light: #E1F5EE;
      --bg: #f9fafb;
      --surface: #ffffff;
      --border: #e5e7eb;
      --text: #111827;
      --muted: #6b7280;
      --user-bubble: #E1F5EE;
      --user-text: #085041;
      --ai-bubble: #f3f4f6;
    }

    body {
      font-family: 'Sora', sans-serif;
      background: var(--bg);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    #app {
      width: 100%;
      max-width: 760px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 16px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      height: 90vh;
      max-height: 760px;
      box-shadow: 0 4px 24px rgba(0,0,0,0.07);
    }

    /* Header */
    #header {
      padding: 16px 20px;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      gap: 12px;
      background: var(--surface);
    }
    #logo {
      width: 36px; height: 36px; border-radius: 10px;
      background: var(--accent-light);
      display: flex; align-items: center; justify-content: center;
    }
    #logo svg { width: 20px; height: 20px; }
    #header-text h1 { font-size: 16px; font-weight: 600; color: var(--text); }
    #header-text p { font-size: 12px; color: var(--muted); margin-top: 2px; }
    #status {
      margin-left: auto; display: flex; align-items: center;
      gap: 6px; font-size: 12px; color: var(--muted);
    }
    #dot { width: 8px; height: 8px; border-radius: 50%; background: var(--accent); }

    /* Upload zone */
    #upload-zone {
      margin: 14px 16px 0;
      border: 1.5px dashed var(--border);
      border-radius: 12px;
      padding: 18px;
      text-align: center;
      cursor: pointer;
      transition: border-color .2s, background .2s;
      background: #fafafa;
    }
    #upload-zone:hover { border-color: var(--accent); background: var(--accent-light); }
    #upload-zone input { display: none; }
    #upload-zone .ub { font-size: 14px; font-weight: 500; color: var(--accent); }
    #upload-zone p { font-size: 12px; color: var(--muted); margin-top: 4px; }

    /* Doc pills */
    #doc-list { margin: 8px 16px 0; display: flex; flex-wrap: wrap; gap: 6px; }
    .doc-pill {
      background: #f3f4f6; border: 1px solid var(--border);
      border-radius: 20px; padding: 4px 10px;
      font-size: 12px; color: var(--muted);
      display: flex; align-items: center; gap: 5px;
    }
    .doc-pill .remove { cursor: pointer; color: #9ca3af; }
    .doc-pill .remove:hover { color: #ef4444; }

    /* Warning */
    #warn {
      display: none; margin: 8px 16px 0;
      font-size: 12px; color: #92400e;
      background: #fef3c7; border-radius: 8px; padding: 6px 12px;
    }

    /* Messages */
    #msgs {
      flex: 1; overflow-y: auto; padding: 16px;
      display: flex; flex-direction: column; gap: 14px;
    }
    .msg { display: flex; flex-direction: column; max-width: 82%; }
    .msg.user { align-self: flex-end; align-items: flex-end; }
    .msg.ai { align-self: flex-start; align-items: flex-start; }
    .msg-label {
      font-size: 11px; color: var(--muted); margin-bottom: 4px;
      font-family: 'JetBrains Mono', monospace;
    }
    .bubble {
      padding: 10px 14px; border-radius: 16px;
      font-size: 14px; line-height: 1.65; color: var(--text);
    }
    .msg.user .bubble { background: var(--user-bubble); color: var(--user-text); border-bottom-right-radius: 4px; }
    .msg.ai .bubble { background: var(--ai-bubble); border: 1px solid var(--border); border-bottom-left-radius: 4px; }
    .source-tag {
      margin-top: 6px; font-size: 11px; color: var(--accent-dark);
      background: var(--accent-light); border-radius: 20px;
      padding: 3px 10px; font-family: 'JetBrains Mono', monospace;
    }

    /* Typing indicator */
    .typing { display: flex; gap: 4px; align-items: center; padding: 10px 14px; }
    .typing span {
      width: 7px; height: 7px; border-radius: 50%;
      background: #9ca3af; animation: blink 1.2s infinite;
    }
    .typing span:nth-child(2) { animation-delay: .2s; }
    .typing span:nth-child(3) { animation-delay: .4s; }
    @keyframes blink { 0%,60%,100%{opacity:.3} 30%{opacity:1} }

    /* Welcome */
    .welcome { text-align: center; padding: 28px 16px; color: var(--muted); }
    .welcome strong { display: block; font-size: 16px; font-weight: 500; color: var(--text); margin-bottom: 6px; }
    .chip-row { display: flex; flex-wrap: wrap; gap: 6px; justify-content: center; margin-top: 12px; }
    .chip {
      font-size: 12px; padding: 6px 14px; border-radius: 20px;
      border: 1px solid var(--border); background: #f9fafb;
      cursor: pointer; color: var(--muted); transition: border-color .15s, color .15s;
    }
    .chip:hover { border-color: var(--accent); color: var(--accent); }

    /* Input area */
    #input-area {
      padding: 12px 16px;
      border-top: 1px solid var(--border);
      display: flex; gap: 10px; align-items: flex-end;
      background: var(--surface);
    }
    #msg-input {
      flex: 1; border: 1px solid var(--border); border-radius: 10px;
      padding: 10px 14px; font-size: 14px; font-family: 'Sora', sans-serif;
      resize: none; min-height: 44px; max-height: 120px;
      background: #f9fafb; color: var(--text); outline: none; line-height: 1.5;
    }
    #msg-input:focus { border-color: var(--accent); background: #fff; }
    #send-btn {
      width: 42px; height: 42px; border-radius: 10px;
      border: none; background: var(--accent); color: #fff;
      cursor: pointer; display: flex; align-items: center; justify-content: center;
      transition: background .2s, transform .1s; flex-shrink: 0;
    }
    #send-btn:hover { background: var(--accent-dark); }
    #send-btn:active { transform: scale(0.95); }
    #send-btn:disabled { background: var(--border); cursor: not-allowed; }
    #send-btn svg { width: 18px; height: 18px; }

    /* API key banner */
    #api-banner {
      background: #eff6ff; border-bottom: 1px solid #bfdbfe;
      padding: 10px 20px; font-size: 12px; color: #1e40af;
      display: flex; align-items: center; gap: 8px;
    }
    #api-banner input {
      flex: 1; border: 1px solid #bfdbfe; border-radius: 6px;
      padding: 5px 10px; font-size: 12px; font-family: 'JetBrains Mono', monospace;
      background: #fff; color: #1e40af; outline: none;
    }
    #api-banner button {
      padding: 5px 12px; border-radius: 6px; border: 1px solid #3b82f6;
      background: #3b82f6; color: #fff; font-size: 12px; cursor: pointer;
    }
  </style>
</head>
<body>
  <div id="app">
    <div id="api-banner">
      <span>🔑 API Key:</span>
      <input type="password" id="api-key-input" placeholder="Enter your Anthropic API key (sk-ant-...)">
      <button onclick="saveKey()">Save</button>
    </div>

    <div id="header">
      <div id="logo">
        <svg viewBox="0 0 24 24" fill="none" stroke="#1D9E75" stroke-width="2" stroke-linecap="round">
          <path d="M12 2L2 7l10 5 10-5-10-5z"/>
          <path d="M2 17l10 5 10-5"/>
          <path d="M2 12l10 5 10-5"/>
        </svg>
      </div>
      <div id="header-text">
        <h1>DocMind – RAG Chatbot</h1>
        <p>Ask questions about your uploaded documents</p>
      </div>
      <div id="status"><div id="dot"></div> AI Ready</div>
    </div>

    <div id="upload-zone" onclick="document.getElementById('file-input').click()">
      <input type="file" id="file-input" accept=".txt,.md" multiple onchange="handleFiles(this.files)">
      <div class="ub">📄 Upload Documents</div>
      <p>Supports .txt and .md files &nbsp;·&nbsp; click to browse</p>
    </div>

    <div id="warn">⚠️ Please upload a document first to enable RAG-powered answers.</div>
    <div id="doc-list"></div>

    <div id="msgs">
      <div class="welcome" id="welcome-msg">
        <strong>Welcome to DocMind 👋</strong>
        Upload a document, then ask anything about it. The AI retrieves relevant context and answers using RAG.
        <div class="chip-row">
          <div class="chip" onclick="tryChip(this)">What is this document about?</div>
          <div class="chip" onclick="tryChip(this)">Summarize the key points</div>
          <div class="chip" onclick="tryChip(this)">What are the main topics?</div>
        </div>
      </div>
    </div>

    <div id="input-area">
      <textarea id="msg-input" placeholder="Ask something about your documents..." rows="1"
        onkeydown="handleKey(event)" oninput="autoResize(this)"></textarea>
      <button id="send-btn" onclick="sendMessage()" title="Send">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <line x1="22" y1="2" x2="11" y2="13"/>
          <polygon points="22 2 15 22 11 13 2 9 22 2"/>
        </svg>
      </button>
    </div>
  </div>

  <script>
    let docs = [];
    let history = [];
    let apiKey = localStorage.getItem('anthropic_key') || '';

    if (apiKey) {
      document.getElementById('api-key-input').value = '••••••••••••••••';
      document.getElementById('api-banner').style.background = '#f0fdf4';
      document.getElementById('api-banner').style.borderColor = '#bbf7d0';
      document.getElementById('api-banner').style.color = '#166534';
    }

    function saveKey() {
      const val = document.getElementById('api-key-input').value.trim();
      if (!val || val.startsWith('•')) return;
      apiKey = val;
      localStorage.setItem('anthropic_key', val);
      document.getElementById('api-key-input').value = '••••••••••••••••';
      document.getElementById('api-banner').style.background = '#f0fdf4';
      document.getElementById('api-banner').style.color = '#166534';
    }

    function handleFiles(files) {
      Array.from(files).forEach(f => {
        const reader = new FileReader();
        reader.onload = e => {
          const existing = docs.findIndex(d => d.name === f.name);
          if (existing >= 0) docs[existing].content = e.target.result;
          else docs.push({ name: f.name, content: e.target.result });
          renderDocs();
        };
        reader.readAsText(f);
      });
    }

    function renderDocs() {
      document.getElementById('doc-list').innerHTML = docs.map(d => `
        <div class="doc-pill">
          📄 ${d.name}
          <span class="remove" onclick="removeDoc('${d.name}')">✕</span>
        </div>`).join('');
      document.getElementById('warn').style.display = 'none';
    }

    function removeDoc(name) {
      docs = docs.filter(d => d.name !== name);
      renderDocs();
    }

    function tryChip(el) {
      document.getElementById('msg-input').value = el.textContent;
      sendMessage();
    }

    function autoResize(el) {
      el.style.height = 'auto';
      el.style.height = Math.min(el.scrollHeight, 120) + 'px';
    }

    function handleKey(e) {
      if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
    }

    function addMsg(role, text, sources) {
      const welcome = document.getElementById('welcome-msg');
      if (welcome) welcome.remove();
      const msgs = document.getElementById('msgs');
      const div = document.createElement('div');
      div.className = `msg ${role}`;
      const label = role === 'user' ? 'You' : 'DocMind AI';
      let inner = `<div class="msg-label">${label}</div><div class="bubble">${text.replace(/\n/g, '<br>')}</div>`;
      if (sources && sources.length)
        inner += sources.map(s => `<div class="source-tag">📍 ${s}</div>`).join('');
      div.innerHTML = inner;
      msgs.appendChild(div);
      msgs.scrollTop = msgs.scrollHeight;
    }

    function showTyping() {
      const msgs = document.getElementById('msgs');
      const div = document.createElement('div');
      div.className = 'msg ai'; div.id = 'typing-indicator';
      div.innerHTML = `<div class="msg-label">DocMind AI</div><div class="bubble"><div class="typing"><span></span><span></span><span></span></div></div>`;
      msgs.appendChild(div);
      msgs.scrollTop = msgs.scrollHeight;
    }

    function removeTyping() {
      const t = document.getElementById('typing-indicator');
      if (t) t.remove();
    }

    async function sendMessage() {
      const input = document.getElementById('msg-input');
      const q = input.value.trim();
      if (!q) return;
      if (!apiKey) { alert('Please enter your Anthropic API key first.'); return; }
      if (docs.length === 0) {
        document.getElementById('warn').style.display = 'block';
        return;
      }

      input.value = '';
      input.style.height = 'auto';
      document.getElementById('send-btn').disabled = true;
      addMsg('user', q);
      history.push({ role: 'user', content: q });
      showTyping();

      const context = docs.map(d => `=== Document: ${d.name} ===\n${d.content.slice(0, 4000)}`).join('\n\n');

      const systemPrompt = `You are DocMind, an expert RAG (Retrieval-Augmented Generation) AI assistant.
Use ONLY the provided document context to answer the user's questions.
If the answer is not in the documents, clearly say so.
Be concise and helpful. Always end your response with: [Source: <document name>]

DOCUMENT CONTEXT:
${context}`;

      try {
        const res = await fetch('https://api.anthropic.com/v1/messages', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-api-key': apiKey,
            'anthropic-version': '2023-06-01',
            'anthropic-dangerous-direct-browser-access': 'true'
          },
          body: JSON.stringify({
            model: 'claude-sonnet-4-20250514',
            max_tokens: 1000,
            system: systemPrompt,
            messages: history
          })
        });
        const data = await res.json();
        if (data.error) throw new Error(data.error.message);
        const reply = data.content?.[0]?.text || 'No response received.';
        const srcMatch = reply.match(/\[Source:\s*([^\]]+)\]/i);
        const cleanReply = reply.replace(/\[Source:[^\]]+\]/gi, '').trim();
        const sources = srcMatch ? [srcMatch[1].trim()] : docs.map(d => d.name);
        removeTyping();
        addMsg('ai', cleanReply, sources);
        history.push({ role: 'assistant', content: reply });
      } catch (err) {
        removeTyping();
        addMsg('ai', `Error: ${err.message}`);
      }
      document.getElementById('send-btn').disabled = false;
      input.focus();
    }
  </script>
</body>
</html>
"""
components.html(html_content, height=900, scrolling=True)
