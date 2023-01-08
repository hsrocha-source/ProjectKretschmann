// uc480Acquire.cpp : Defines the class behaviors for the application.
//

#include "stdafx.h"
#include "uc480Acquire.h"
#include "uc480AcquireDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// Cuc480AcquireApp

BEGIN_MESSAGE_MAP(Cuc480AcquireApp, CWinApp)
	//{{AFX_MSG_MAP(Cuc480AcquireApp)
		// NOTE - the ClassWizard will add and remove mapping macros here.
		//    DO NOT EDIT what you see in these blocks of generated code!
	//}}AFX_MSG
	ON_COMMAND(ID_HELP, CWinApp::OnHelp)
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// Cuc480AcquireApp construction

Cuc480AcquireApp::Cuc480AcquireApp()
{
	// TODO: add construction code here,
	// Place all significant initialization in InitInstance
}

/////////////////////////////////////////////////////////////////////////////
// The one and only Cuc480AcquireApp object

Cuc480AcquireApp theApp;

/////////////////////////////////////////////////////////////////////////////
// Cuc480AcquireApp initialization

BOOL Cuc480AcquireApp::InitInstance()
{
	AfxEnableControlContainer();

	// Standard initialization
	// If you are not using these features and wish to reduce the size
	//  of your final executable, you should remove from the following
	//  the specific initialization routines you do not need.


/*	// Enable3dControls and Enable3dControlsStatic are no longer necessary.
#ifdef _AFXDLL
	Enable3dControls();			// Call this when using MFC in a shared DLL
#else
	Enable3dControlsStatic();	// Call this when linking to MFC statically
#endif
	*/

	Cuc480AcquireDlg dlg;
	m_pMainWnd = &dlg;
	INT_PTR nResponse = dlg.DoModal();
	if (nResponse == IDOK)
	{
		// TODO: Place code here to handle when the dialog is
		//  dismissed with OK
	}
	else if (nResponse == IDCANCEL)
	{
		// TODO: Place code here to handle when the dialog is
		//  dismissed with Cancel
	}

	// Since the dialog has been closed, return FALSE so that we exit the
	//  application, rather than start the application's message pump.
	return FALSE;
}
