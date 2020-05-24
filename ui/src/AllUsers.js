import React from 'react';
import './App.css';
import User from './components/user/user'
import Snapshot from "./components/snapshot/snapshot";
import {Backdrop, Fade, Modal} from "@material-ui/core";


class AllUsers extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            users: null,
            displaySnapshot: false,
            displayUserId: null
        };
        this.close_snapshot = this.close_snapshot.bind(this)

    };


    render_users() {
        const all_users = this.state.users.map((user) =>

            <User userId={user.userId} onClick={this.display_snapshots.bind(this, user.userId)}/>
        );
        return <div>{all_users}</div>
    }


    display_snapshots(user_id) {
        this.setState({displaySnapshot: true, displayUserId: user_id})
    }

    close_snapshot() {
        this.setState({displaySnapshot: false});
    }

    render() {

        if (this.state.users == null) {
            return 'loading ...';
        }
        return (
            <React.Fragment>
                {this.state.users.map((user) =>
                    <User key={user.userId} userId={user.userId} onClick={this.display_snapshots.bind(this, user.userId)}/>)
                }
                <Modal open={this.state.displaySnapshot}
                       onClose={this.close_snapshot}

                       >

                        <Snapshot userId={this.state.displayUserId} close={this.close_snapshot}/>


                </Modal>
            </React.Fragment>
        );
    }


    componentDidMount() {
        fetch(`${window.apisrv}/users`)
            .then(response => response.json())
            .then(data => this.setState({users: data}));
    }
}

export default AllUsers;
