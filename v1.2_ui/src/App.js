import { useState } from 'react';
import callLLM from './services/LLMService';
import './App.css'
import Input from './components/Input'
import Output from './components/Output'

export default function App() {
  function handleSubmit(event, userInput) {
    event.preventDefault();
    setOutput(callLLM(userInput));
  }

  const [output, setOutput] = useState('');

  return (
    <div className="maxHeight">
        <div className='d-flex justify-content-around align-items-center text-left text-primary mx-5'>
          <h1><a href="https://github.com/LarryBattle/DocuDive">DocuDive</a></h1>
          <Input handleSubmit={handleSubmit}/>
        </div>
        <Output outputText={output}/>
    </div>
  );
}
