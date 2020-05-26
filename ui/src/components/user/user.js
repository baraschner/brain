import React from 'react';
import Card from '@material-ui/core/Card';
import Box from '@material-ui/core/Box';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';


class User extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            user: null
        }

    }

    render_gender(gender) {
        if (gender === "MALE") {
            return <img src="https://img.icons8.com/bubbles/50/000000/male.png"/>
        }
        return <img src="https://img.icons8.com/bubbles/50/000000/female.png"/>
    }

    render() {
        if (this.state.user == null) {
            return 'loading...'
        }
        return (
            <Box width={1 / 4} m={4}>
                <Card>
                    <CardContent>
                        <Typography variant={'h6'}>
                            {this.state.user.username}
                        </Typography>
                        <Typography color="textSecondary">{this.state.user.userId}</Typography>
                        <Typography>{this.render_gender(this.state.user.gender)}</Typography>
                        <img src="https://img.icons8.com/bubbles/50/000000/birthday.png"/>{new Date(1000 * this.state.user.birthday).toDateString()}
                    </CardContent>

                    <CardActions>
                        <Button color='primary' variant='contained' onClick={this.props.onClick}>Display
                            Snapshots</Button>
                    </CardActions>
                </Card>
            </Box>
        );
    }

    componentDidMount() {
        fetch(`${window.apisrv}/users/${this.props.userId}`)
            .then(response => response.json())
            .then(data => this.setState({user: data}));
    }


}


export default User;



