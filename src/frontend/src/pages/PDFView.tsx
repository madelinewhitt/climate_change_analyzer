import React, { useState } from 'react';
import { Document, Page, pdfjs } from 'react-pdf';

// Use a CDN link for the PDF worker
pdfjs.GlobalWorkerOptions.workerSrc = 'https://cdn.jsdelivr.net/npm/pdfjs-dist@2.8.335/build/pdf.worker.min.js';

const PdfViewer: React.FC = () => {
    const [numPages, setNumPages] = useState<number | null>(null);
    const [pageNumber, setPageNumber] = useState<number>(1);
    const filePath = "../../../../ProjectReport.pdf"; // Adjust path as needed

    function onDocumentLoadSuccess({ numPages }: { numPages: number }) {
        setNumPages(numPages);
    }

    return (
        <div style={{ textAlign: 'center' }}>
            <h1>Project Report PDF Viewer</h1>
            <Document file={filePath} onLoadSuccess={onDocumentLoadSuccess}>
                <Page pageNumber={pageNumber} />
            </Document>
            <div>
                <p>
                    Page {pageNumber} of {numPages}
                </p>
                <button
                    type="button"
                    disabled={pageNumber <= 1}
                    onClick={() => setPageNumber(pageNumber - 1)}
                >
                    Previous
                </button>
                <button
                    type="button"
                    disabled={pageNumber >= (numPages || 1)}
                    onClick={() => setPageNumber(pageNumber + 1)}
                >
                    Next
                </button>
            </div>
        </div>
    );
};

export default PdfViewer;
