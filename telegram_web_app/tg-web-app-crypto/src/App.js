import './App.css';

import React, { useEffect } from 'react';
const tg = window.Telegram.WebApp;

function App() {
  useEffect(() => {
    tg.ready();
  }, []);
  const onClose = () => {
    tg.close();
  }

  return (
    <div className="App">
      <butto onClick={onClose}>Закрыть</butto>
    </div>
  );
}

export default App;
