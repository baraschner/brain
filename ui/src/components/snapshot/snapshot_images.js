import React from 'react';
import GridList from '@material-ui/core/GridList';
import GridListTile from '@material-ui/core/GridListTile';
import GridListTileBar from '@material-ui/core/GridListTileBar';



class SnapshotImages extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            pose: null,
        };
    }

    componentDidMount() {
        fetch(`${window.apisrv}/users/${this.props.userId}/snapshots/${this.props.snapshotId}/colorImage/data`)
            .then(response => response.json())
            .then(data => this.setState({feelings: data}));
    };

    render() {

        return (
            <GridList>
                <GridListTile>
                    <GridListTileBar title="Color Image"/>
                    <img width={200} height={200} alt="Color Image"
                                    src={`${window.apisrv}/users/${this.props.userId}/snapshots/${this.props.snapshotId}/colorImage/data`}/>
                </GridListTile>
                <GridListTile>
                    <GridListTileBar title="Depth Image" />

                    <img width={200} height={200} alt="Depth Image"
                         src={`${window.apisrv}/users/${this.props.userId}/snapshots/${this.props.snapshotId}/depthImage/data`}/>
                </GridListTile>
            </GridList>
        );

    }

}

export default SnapshotImages;
