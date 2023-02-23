import React, { useEffect, useState } from "react";

import Editor from "@monaco-editor/react";
import './Editor.css'

const CodeEditorWindow = ({ language, code}) => {
  const defaultVal =  
  "start bro\n\
  bol bro 'Hello world';\n\n\
  a -> 12;\n\
  b -> 9;\n\
  c -> (a*b)+5;\n\
  bol bro c;\n\n\
  jotokhon bro b<a{\n\
      jodi bro b<10{\n\
        bol bro 'b less than 10';\n\
      }\n\
      jodi na bro b==10{\n\
        bol bro 'b equals to 10';\n\
      }\n\
      na hole bro{\n\
        bol bro 'b greater than 10';\n\
      }\n\
      b = b+1;\n\
  }\n\
  stop bro"

  const [value, setValue] = useState(defaultVal || "");
  const [output, setOutput] = useState('Output will Show here...');

  const handleEditorChange = (value) => {
    setValue(value);

  };

  useEffect(()=>{
    const button = document.getElementById("runbt");
    button.addEventListener("click", runCode({value}));
  },[]);

  const API_URL = 'https://broCodebackend.onrender.com/interpret'

  const runCode = async (value) => {
    const v = value.value
    console.log(v)

    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'text/plain'
      },
      body: v
    };
    const response = await fetch(API_URL,options)
    const data = await response.text();
    setOutput(data);
  };    

  return (
    <>
    <div className="overlay rounded-md overflow-hidden w-full h-full shadow-4xl codeEditor border border-white rounded rounded-4">
      <Editor
        height="60vh"
        width={`100%`}
        language={language || "python"}
        value={value}
        theme= "vs-dark"
        defaultValue= {defaultVal}
        onChange={handleEditorChange}
        options={{
          fontSize: 16
        }}
      />
      <div className="run">
        <button onClick={()=>runCode({value})} id="runbt" className="btn btn-success btn-lg runbutton">Run</button>
      </div>
    </div>
    <h5 className="outputText">Output</h5>
    <div className="overlay rounded-md overflow-hidden w-full h-full shadow-4xl codeEditor border border-white rounded rounded-4">
      <Editor
        height="15vh"
        defaultLanguage="python"
        value={output}
        theme= "vs-dark"
        readOnly={true}
        options={{
          fontSize: 17
        }}
      />
    </div>
    </>
  );
};
export default CodeEditorWindow;