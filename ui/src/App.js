import React from 'react';
import './App.css';
import AllUsers from './AllUsers.js'
import AppBar from '@material-ui/core/AppBar';
import ToolBar from '@material-ui/core/Toolbar';


class App extends React.Component {

    render() {

        return (
            <React.Fragment>
                <AppBar position="static">
                    <ToolBar>
                        <img alt="" src="brain.png" width='45' height='45'/>
                        Brain
                    </ToolBar>
                </AppBar>
                <AllUsers/>
            </React.Fragment>
        );
    }

}


export default App;
