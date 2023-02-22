import {React, useEffect, useState} from "react";
import './App.css';
import CodeEditorWindow from "./components/Editor";
import DocsCard from "./components/DocsCard";

const App = () => {

    const startCode = "start bro\n\nstop bro"
    const printCode = "start bro\n bol bro 'Hello World';\nstop bro"
    const variableCode = "start bro\n a->10;\n b->8.5;\n c-> 'hello';\nstop bro"
    const ifCode = "start bro\na -> 12;\nb -> 10;\njodi bro a<b{\n  bol bro 'less';\n}\njodi na bro a==b{\n  bol bro 'equal';\n}\nna hole bro{\n  bol bro 'greater';\n}\nstop bro"
    const loopCode = "start bro\na -> 12;\nb -> 20;\njotokhon bro a<b{\n  bol bro a;\n  a -> a+1;\n}\nstop bro"
    const assignCode = "start bro\n a -> 10;\n b->12;\n a->b;\nstop bro"
    const assign = "->"

    return (
        <div>
        <div className="app">
            <div className="content">
                <h2><i>BroCode</i></h2>
                <h2><i>BroCode</i></h2>
            </div>

            <div className="Tagline">
                <p>A toy programming language based on inside jokes</p>
                <span className="highlighter"></span>
            </div>
            <br></br>

            <div className="grid mt-2">
                <a href="#playground" type="button" className="btn btn-lg btn-success playButton">
                    Playground
                </a>
                <a href="#download" type="button" className="btn btn-lg btn-light downloadButton">
                    Download
                </a>
            </div>

            <div className="madeby">
                <p>Made by Sujoy Nath <a href="https://sujoynath.me/"><span className="madebyLink">@c0mrd</span></a></p>
            </div>
            
        </div>

        <div className="playground" id="playground">
                {/* <div className="message-list">
                    <div className="message -left">
                        <div className="nes-balloon from-left">
                            <p>Playground</p>
                        </div>
                    </div>
                </div> */}
                <p>Playground</p>
        </div>
        <CodeEditorWindow  />
        <br></br>
        <h2 className="documentText">Documentation</h2>
        <div className="docs">
            <DocsCard heading="General"
                        explain={<><span>start bro</span> is the entrypoint for the program and all program must end with <span>stop bro</span>. Anything outside of it will be ignored</>}
                        code={startCode}
                        height="25vh" />

            <DocsCard heading="Built-ins"
                        explain={<>Use <span>bol bro</span> to print anything to console.</>}
                        code={printCode}
                        height="25vh" />

            <DocsCard heading="Variables"
                        explain={<>Variables can be declared or assigned using <span>{assign}</span> operator </>}
                        code={assignCode}
                        height="25vh" />

            <DocsCard heading="Types"
                        explain={<>Supports <span>int</span> , <span>float</span> , <span>string</span> types</>}
                        code={variableCode}
                        height="25vh" />

            <DocsCard heading="Conditionals"
                        explain={<>BroCode supports if-else-if ladder construct , <span>jodi bro</span> will execute if condition, <span>jodi na bro</span> equivalet to elseif and <span>na hole bro </span> equivalent to else. </>}
                        code={ifCode}
                        height="25vh" />

            <DocsCard heading="Loops"
                        explain={<>Statements inside <span>jotokhon bro</span> blocks are executed as long as a specified condition evaluates to true.</>}
                        code={loopCode}
                        height="25vh" />
            
        </div>

        <div>
            <h2 className="documentText">Download</h2>
            <div className="download" id="download">
                <p>Will be available very soon...</p>
            </div>
        </div>
        

        </div>
    );
}

export default App;