import React from 'react';
import Layout from './layout';
import UploadFiles from '../components/UploadFiles';
import MetadataViewer from '../components/MetadataViewer';
import CatalogViewer from '../components/CatalogViewer';
import ReportViewer from '../components/ReportViewer';

const Page: React.FC = () => {
    return (
        <Layout>
            <UploadFiles />
            <MetadataViewer />
            <CatalogViewer />
            <ReportViewer />
        </Layout>
    );
};

export default Page;
