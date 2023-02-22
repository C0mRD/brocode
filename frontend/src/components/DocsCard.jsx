import React, { useState } from "react";

import Editor from "@monaco-editor/react";

const DocsCard = ({ heading, explain, code, height}) => {

  return (
          <div className="docsDiv card">
                <hr></hr>
                <h5 className="card-header">{heading}</h5>
                <div className="card-body">
                    <p className="card-text">{explain}</p>
                </div>
                
                <Editor
                    height={height}
                    defaultLanguage="python"
                    value={code}
                    theme= "vs-dark"
                    readOnly={true}
                    options={{
                        fontSize: 17
                    }}
                />
                <hr></hr>
            </div>
  );
};
export default DocsCard;